from dotenv import load_dotenv, find_dotenv
import os
import pprint as printer
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PASS")

connection_string = f"mongodb+srv://admin:{password}@cs410project.wos3sy2.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

dbs = client.list_database_names()

database = client.data # Database that contains the collections

# collections = database.list_collection_names()
# print(collections)

collection = database.courses # The collection within the database

def insert_entry():
  test_entry = {
    "name": "CS 410",
    "level": 400,
    "professor": "Placeholder",
    "credit hours": 3,
    "prereq": "placeholder",
    "semester": "Fall",
    "year": "2022",
    "description": "Theory, design, and implementation of text-based information systems. Text analysis, retrieval models (e.g., Boolean, vector space, probabilistic), text categorization, text filtering, clustering, retrieval system design and implementation, and applications to web information management. 3 undergraduate hours. 3 or 4 graduate hours. Prerequisite: CS 225."
  }

  collection.insert_one(test_entry)

insert_entry()

def insert_multiple_entries():
  courses = ["CS 110", "CS 220", "CS 330", "CS 440", "CS 550"]
  levels = [100, 200, 300, 400, 500]
  descriptions = ["a", "b", "c", "d", "e"]

  docs = []

  for name, lev, desc in zip(courses, levels, descriptions):
    doc = {"name": name, "level": lev, "description": desc}
    docs.append(doc)

  collection.insert_many(docs)

# insert_multiple_entries()

def query_db():
  course = collection.find_one({"name": "CS 410"})
  print(course['description'])
  printer.pprint(course)

# query_db()

def filter_db(min_level, max_level):
  query = {"$and": [
    {"level": {"$gte": min_level}},
    {"level": {"$lte": max_level}}
  ]}

  course = collection.find(query).sort("level")

  for c in course:
    printer.pprint(c)

# filter_db(400, 600)

review = {
  "rating": 5,
  "difficulty": 3
}

def add_review(course_id, review):
  from bson.objectid import ObjectId

  _id = ObjectId(course_id)

  collection.update_one(
    {"_id": _id}, {"$addToSet": {'reviews': review}}
  )

# Change the course_id
add_review("63606b8c3c11c14f3f2903bf", "Interesting course to learn about text retrieval and NLP. Highly recommended!")

def add_review_as_relationship(course_id, review):
  from bson.objectid import ObjectId
  _id = ObjectId(course_id)

  review = review.copy()
  review["course_id"] = _id

  review_collection = database.reviews
  review_collection.insert_one(review)

# Change the course_id
add_review_as_relationship("6359e4235cb1963f485d00c0", {"rating": 4, "difficulty": 4})

