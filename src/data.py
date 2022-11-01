from dotenv import load_dotenv, find_dotenv
import os
import pprint as printer
from pymongo import MongoClient
from bs4 import BeautifulSoup

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PASS")

connection_string = f"mongodb+srv://admin:{password}@cs410project.wos3sy2.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

html_doc = ""
soup = BeautifulSoup(html_doc, 'html.parser')

def one_to_two_courses():
  return

def three_to_four_courses():
  return

def five_courses():
  return
