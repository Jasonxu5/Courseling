from tkinter import N
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
from output import prereqs_list

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

prereqs = prereqs_list

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

# for course in soup.findAll('div', class_ = 'courseblock'):
#   preq = []
#   level = course.find('a', class_ = 'schedlink')
#   level = int(level.text[3:6])
#   if level >= 300 and level < 500:
#     prereq = course.select('p.courseblockdesc > a')
#     for _ in prereq:
#       curr = unicodedata.normalize("NFKD", _.text)
#       preq.append(curr)
#     prereqs.append(preq)

# with open('output.txt', 'w') as f:
#   for line in prereqs:
#     f.write(f"{line}\n")

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
  desc = soup.select_one('div#extCoursesDescription > div.extCoursesProfileContent')

  if instructor != None and date != None and desc != None:
    professors.append(instructor.text)
    semester = date.text.split()[0]
    year = date.text.split()[1]

    semesters.append(semester)
    years.append(int(year))
    descriptions.append(desc.text)
  else:
    professors.append("N/A")
    semesters.append("N/A")
    years.append("N/A")
    descriptions.append("N/A")


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
  courses = ["CS 210", "CS 211" , "CS 222", "CS 225", "CS 233"]
  levels = [200, 200, 200, 200, 200]
  descriptions = ["Ethics for the computing profession. Ethical decision-making; licensing; intellectual property, freedom of information, and privacy. Course Information: Credit is not given for both CS 210 and either CS 211 or ECE 316. Prerequisite: CS 225. Junior standing required.",
  "Navigating the complex ethical and professional landscape of the computing professional: privacy, intellectual property, cybersecurity, and freedom of speech. Hands-on exercises, assignments, and discussions in which students analyze current events from perspectives in both philosophical and professional ethics. Writing professionally and technically in several writing assignments requiring peer review, workshops, and multiple rounds of editing and revising.",
  "Design and implementation of novel software solutions. Problem identification and definition; idea generation and evaluation; and software implementation, testing, and deployment. Emphasizes software development best practices?including framework selection, code review, documentation, appropriate library usage, project management, continuous integration and testing, and teamwork.",
  "Data abstractions: elementary data structures (lists, stacks, queues, and trees) and their implementation using an object-oriented programming language. Solutions to a variety of computational problems such as search on graphs and trees. Elementary analysis of algorithms",
  "Fundamentals of computer architecture: digital logic design, working up from the logic gate level to understand the function of a simple computer; machine-level programming to understand implementation of high-level languages; performance models of modern computer architectures to enable performance optimization of software; hardware primitives for parallelism and security."] 
  
  professors = ["Ryan Matthew Cunningham","Ryan Matthew Cunningham","Michael Joseph Woodley",["Graham Carl Evans","Wade A Fagen-Ulmschneider"],["Geoffrey Lindsay Herman","Craig Zilles"]]
  credit_hours = [[2,3],[2,3],1,4,4]
  prerequisites = ["CS 225","CS 225","CS 128",["CS 126","CS 128 ","ECE 220", "CS 173", "MATH 213","MATH 347","MATH 412", " MATH 413"],["CS 125","CS 128","CS 173","MATH 213"]]
  semesters = ["Fall","Fall","FALL","FALL","FALL"]
  years = ["2022","2022", "2022", "2022", "2022"]

  docs = []

  for name, lev, desc, professor, credit_hour, prereq, sem, yr in zip(courses, levels, descriptions, professors, credit_hours,prerequisites,semesters,years):
    doc = {"name": name, "level": lev,  "professor": professor,
          "credit hours": credit_hour, "prereq": prereq, 
          "semester":sem, "year":yr, "description": desc}
    docs.append(doc)

  collection.insert_many(docs)

one_to_two_courses()

def three_to_four_courses():
  docs = []

  for n, l, p, ch, pr, s, y, d in zip(courses, levels, professors, credit_hours, prereqs, semesters, years, descriptions):
    doc = {"name": n, "level": l, "professor": p, "credit hours": ch, "prereq": pr, "semester": s, "year": y, "description": d}
    docs.append(doc)

  collection.insert_many(docs)

three_to_four_courses()


def five_courses():
  return
