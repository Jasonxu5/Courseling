import json
from os import path
import os

import flask
from bson import json_util
from dotenv import find_dotenv, load_dotenv
from flask import Flask, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from pymongo import MongoClient

import subprocess

app = Flask(__name__)
CORS(app)
load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PASS")
connection_string = f"mongodb+srv://admin:{password}@cs410project.wos3sy2.mongodb.net/?retryWrites=true&w=majority"
mongodb_client = MongoClient(connection_string)
dbs = mongodb_client.list_database_names()

database = mongodb_client.data.courses

# Members API Route
@app.route("/members")
def members():
    return{"members": ["Member1", "Member2", "Member3"]}

@app.route("/")
def home():
    collection = database
    cursor = collection.find({})
    return json.loads(json_util.dumps([document for document in cursor]))

@app.route("/courses")
def courses():
    args = request.args
    type(args.to_dict())
    input = args.get("query")
    input = '"' + input + '"'
    try:
        subprocess.call(f"python search_eval.py {input}")
        file = open('results.txt', 'r')
        data = file.read()
    except TypeError:
        return {"description" : "Query not found"}
    dataTest = json.loads(data)
    print(dataTest)
    return json.loads(data)

@app.route("/search")
def search():
    args = request.args
    type(args.to_dict())
    query = args.get("query").upper()

    try:
        course = database.find_one({"name": query})
        print(course['description'])
    except TypeError:
        return {"description": "Course not found"}
    return json.loads(json_util.dumps(course))

if __name__ == "__main__":
    app.run(debug=True)