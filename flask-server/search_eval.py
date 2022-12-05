"""
To do: How to input a query dynamically?
To do: Need to cd into data folder for the script to "config.toml". How to bypass this?
To do: How/what format to pass ranked list to flask?
This function creates a ranked list of (mongodb_id, ranking score) pairs in relation to a query
"""

import metapy
import pytoml
import sys
import pandas as pd
import json

def load_ranker(cfg_file):
    """
    Use this function to return the Ranker object to evaluate.
    The parameter to this function, cfg_file, is the path to a
    configuration file used to load the index.
    """
    return metapy.index.OkapiBM25()

def search(cfg_file, search_phrase):
    print('Building or loading index...')

    #Create the inverted index for the dataset
    idx = metapy.index.make_inverted_index(cfg_file)

    #Check idx
    print("# docs in idx: ", str(idx.num_docs()))
    print("# unique terms in idx: ", str(idx.unique_terms()))
    print("Avg doc length in idx: ", str(idx.avg_doc_length()))
    print("Total corpus terms in idx: ", str(idx.total_corpus_terms()))

    #Create Ranker object
    ranker = load_ranker(cfg_file)

    #Evaluate relevance judgements for the queries
    ev = metapy.index.IREval(cfg_file)

    #Set paths
    with open(cfg_file, 'r') as fin:
        cfg_d = pytoml.load(fin)

    query_cfg = cfg_d['query-runner']
    if query_cfg is None:
        print("query-runner table needed in {}".format(cfg))
        sys.exit(1)

    # start_time = time.time()
    query_path = query_cfg.get('query-path', 'course-queries.txt')
    query_start = query_cfg.get('query-id-start', 1)

    #Create Document object and set its content with the query
    query = metapy.index.Document()
    query.content(search_phrase.strip())

    #Search index using the ranker and query
    top_docs = ranker.score(idx, query, num_results=5)
    print("Query: ", str(search_phrase))
    print("Search results: ", str(top_docs))

    #Runs stats for batch of queries in course-queries.txt
    num_queries = 0
    qresults = []
    print('Running queries')
    with open(query_path) as query_file:
        for query_num, line in enumerate(query_file):
            query.content(line.strip())
            results = ranker.score(idx, query, num_results=5)
            # print("search results:", results)
            q_precision = ev.precision(results, query_start + query_num, 5)
            q_recall = ev.recall(results, query_start + query_num, 5)
            q_f1 = ev.f1(results, query_start + query_num, 5)
            q_avg_p = ev.avg_p(results, query_start + query_num, 5)
            num_queries+=1
            qresults.append(q_avg_p)
            print("Query {} average precision: {}".format(query_num + 1, q_avg_p))
            print("Query {} precision: {}".format(query_num + 1, q_precision))
            print("Query {} recall: {}".format(query_num + 1, q_recall))
            print("Query {} F1 score: {}".format(query_num + 1, q_f1))
    # ev.map()
    return top_docs

if __name__ == "__main__":
    #cfg = sys.argv[1]
    cfg = 'config.toml'
    input = sys.argv[1]
    search_results = search(cfg, input)

    #Get the mongodb ID that corresponds to ranked search_results ID
    columns = ['id','_id','name']
    course_data = pd.DataFrame(columns=columns)
    with open('courses/courses.dat') as f:
        for line in f:
            course_data.loc[len(course_data)] = line.split(",")[:3]
    #print(course_data)

    db_search_results = {}
    if search_results:
        for result in search_results:
            index = result[0]
            db_search_results[course_data.iloc[index]["name"]] =  result[1]
    print("Search results w/ Mongo DB id: ", db_search_results)
    f = open("results.txt", "w")
    f.write(json.dumps(db_search_results))
    f.close()