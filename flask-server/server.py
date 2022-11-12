from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_pymongo import PyMongo
from bson import json_util
from pymongo import MongoClient
import flask
import json
import os

app = Flask(__name__)
load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PASS")
connection_string = f"mongodb+srv://admin:{password}@cs410project.wos3sy2.mongodb.net/?retryWrites=true&w=majority"
mongodb_client = MongoClient(connection_string)
dbs = mongodb_client.list_database_names()

database = mongodb_client.data

# Members API Route
@app.route("/members")
def members():
    return{"members": ["Member1", "Member2", "Member3"]}

@app.route("/")
def home():
    collection = database.courses
    cursor = collection.find({})
    return json.loads(json_util.dumps([document for document in cursor]))

if __name__ == "__main__":
    app.run(debug=True)