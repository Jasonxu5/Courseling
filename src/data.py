from dotenv import load_dotenv, find_dotenv
import os
import pprint as printer
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unicodedata

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PASS")

connection_string = f"mongodb+srv://admin:{password}@cs410project.wos3sy2.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
database = client.data

# html_doc = requests.get("https://cs.illinois.edu/academics/courses")
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Firefox(executable_path="C:\\Users\\Jason\Downloads\\geckodriver-v0.32.0-win64\\geckodriver.exe")

driver.get("http://catalog.illinois.edu/courses-of-instruction/cs/")
# button = driver.find_element(By.XPATH, '//*[@id="tcat-tab"]').click()
time.sleep(1)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

courses = []
levels = []
professors = []
credit_hours = []
prereqs = []
semesters = []
years = []
descriptions = []

for i in range(79):
  prereqs.append("N/A")

for a in soup.findAll('a', class_ = 'schedlink'):
  for b in a:
    course_level = int(b.text[3:6])
    if course_level >= 300 and course_level < 500:
      course_name = unicodedata.normalize("NFKD", b.text[:6])
      courses.append(course_name)
      if course_level < 400:
        levels.append(300)

      if course_level >= 400 and course_level < 500:
        levels.append(400)

      credits = b.text.find('credit')
      credit_hours.append(int(b.text[credits + 8]))

# course_elements = []
for c in soup.findAll('div', class_ = 'courseblock'):
  for d in c:
    level = c.find('a', class_ = 'schedlink')
    level = int(level.text[3:6])
    if level >= 300 and level < 500:
      desc = c.find('p', class_ = 'courseblockdesc')
      desc = unicodedata.normalize("NFKD", desc.text)
      desc = desc.strip()
      descriptions.append(desc)

driver.get('https://cs.illinois.edu/academics/courses')
driver.find_element(By.XPATH, '//*[@id="tcat-tab"]').click()
time.sleep(1)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# cs_courses = soup.select('div#tcat > div > table > tbody > tr > td.rubric > a')

for i in courses:
  i = ''.join(i.split())
  driver.get(f"https://cs.illinois.edu/academics/courses/{i}")
  # time.sleep(1)
  page_source = driver.page_source
  soup = BeautifulSoup(page_source, 'html.parser')
  instructor = soup.select_one('td.extCoursesTTinstr > a')
  date = soup.select_one('h3')

  if instructor != None and date != None:
    professors.append(instructor.text)
    semester = date.text.split()[0]
    year = date.text.split()[1]

    semesters.append(semester)
    years.append(int(year))
  else:
    professors.append("N/A")
    semesters.append("N/A")
    years.append("N/A")


print(courses)
print(levels)
print(credit_hours)
print(descriptions)
print(professors)
print(len(professors))
print(semesters)
print(len(semesters))
print(years)
print(len(years))
# print(prereqs)

def one_to_two_courses():
  return

collection = database.test
def three_to_four_courses():
  docs = []

  for n, l, p, ch, pr, s, y, d in zip(courses, levels, professors, credit_hours, prereqs, semesters, years, descriptions):
    doc = {"name": n, "level": l, "professor": p, "credit hours": ch, "prereq": pr, "semester": s, "year": y, "description": d}
    docs.append(doc)

  collection.insert_many(docs)

three_to_four_courses()


def five_courses():
  return
