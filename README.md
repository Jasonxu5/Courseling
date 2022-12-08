# Courseling

Courseling is a Google Chrome extension that allows the user to perform searches for computer science courses at the University of Illinois Urbana-Champaign. There are two primary search functions available to the user:

1. The user can input an arbitrary query, receiving a ranked list of the Top 5 courses that are most relevant to the user's query.
2. A specific course can be queried, which returns a detailed description of the course, including things like its credit hours, semesters offered, etc.


## Build and Run the Extension
1. Clone the repo to the desired directory (`git clone https://github.com/Jasonxu5/Courseling.git`)
2. In a terminal, cd to the Courseling repo and MAKE sure you are in the root repo
    - If you run `ls`, you should see the output of `client`, `data`, `flask-server`, etc.
3. Run command `pip install -r requirements.txt` which will install all the required Python modules
4. Next, make sure you have npm installed (https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
5. Navigate to the `client` folder and then run the command `npm run build`
6. The command should generate a new `build` folder in the client folder
7. Go to `chrome://extensions` and make sure developer mode is enabled
8. Click on the option to "Load unpacked" and select the `build` folder that you just generated
9. Now go back to the repo and navigate to the `flask-server` folder
10. Run the command `python server.py` and this should start up the flask server
11. Now click on the extension (the icon looks like a mortarboard on top of a screen). You can pin the extension for easier access.
12. You should then be able to make queries and get a output of the top courses and their scores


## Architecture Overview
In order to collect the required data to train our text retrieval ranking function, we used a MongoDB NoSQL database to store all of the computer science courses at UIUC and their relevant information.

The underlying architecture of the extension follows the client-server model. On the backend, there is a server built using Flask in Python. We utilize the BM25 algorithm provided by the metapy library to perform ranking logic on the user's input, generating either a list of courses or directly indexing our database to return all information related to that specific course. The output of this logic is sent to the frontend Google Chrome extension client interface built in JavaScript. From there, it is rendered and displayed underneath the search bar.

### Technology/Library Usage
1. MongoDB
2. beautifulsoup4 - 4.11.1
2. Flask - 2.2.2
3. Flask_Cors - 3.0.10
4. Flask_PyMongo - 2.3.0
5. metapy - 0.2.13
6. pandas - 1.3.5
7. pymongo - 4.3.2
8. pytoml - 0.1.21
9. requests - 2.22.0
10. selenium - 4.7.2


## Task Allocation
| Task           | Team Members |
| :------------: | :------------: |
| Data Collection/Manipulation | Andrew Ko, Jason Xu, Nick Chun, Sahil Agrawal |
| Frontend UI | Andrew Ko, Jason Xu |
| Flask Server | Sahil Agrawal, Sophia Yu |
| Ranking Function | Sahil Agrawal, Sophia Yu |
| Documentation | Jason Xu, Nick Chun |
| Demonstration | Nick Chun |