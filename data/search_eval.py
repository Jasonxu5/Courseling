"""
Needs dataset in MeTA format (*.dat) with courses folder
This function creates a ranked list of (doc_id, score) pairs in relation to a query
"""

import metapy
import pytoml
import sys

def load_ranker(cfg_file):
    """
    Use this function to return the Ranker object to evaluate.
    The parameter to this function, cfg_file, is the path to a
    configuration file used to load the index.
    """
    return metapy.index.OkapiBM25()

if __name__ == '__main__':
    cfg = 'config.toml'
    print('Building or loading index...')

    #Create the inverted index for the dataset
    idx = metapy.index.make_inverted_index(cfg)

    #Check idx
    print("# docs in idx: " + str(idx.num_docs()))
    print("# unique terms in idx: " + str(idx.unique_terms()))
    print("Avg doc length in idx: " + str(idx.avg_doc_length()))
    print("Total corpus terms in idx: " + str(idx.total_corpus_terms()))

    #Create Ranker object
    ranker = load_ranker(cfg)

    # No relevance judgements for the queries?
    # ev = metapy.index.IREval(cfg)

    #Set paths
    with open(cfg, 'r') as fin:
        cfg_d = pytoml.load(fin)

    query_cfg = cfg_d['query-runner']
    if query_cfg is None:
        print("query-runner table needed in {}".format(cfg))
        sys.exit(1)
    
    # start_time = time.time()
    top_k = 10
    query_path = query_cfg.get('query-path', 'queries.txt')
    query_start = query_cfg.get('query-id-start', 0)

    #Create Document object and set its content with the query
    query = metapy.index.Document()
    query.content('text systems')

    #Search index using the ranker and query
    top_docs = ranker.score(idx, query, num_results=2)
    print(top_docs)

    # ndcg = 0.0
    # num_queries = 0
    # print('Running queries')
    # with open(query_path) as query_file:
    #     for query_num, line in enumerate(query_file):
    #         query.content(line.strip())
    #         results = ranker.score(idx, query, top_k)
    #         ndcg += ev.ndcg(results, query_start + query_num, top_k)
    #         num_queries+=1
    # ndcg= ndcg / num_queries
    # print("NDCG@{}: {}".format(top_k, ndcg))
    # print("Elapsed: {} seconds".format(round(time.time() - start_time, 4)))