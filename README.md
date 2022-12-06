# Courseling

### Build and Run the Extension
1. Clone the repo to the desired directory (`https://github.com/Jasonxu5/Courseling.git`)
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
11. Now click on the extension (the icon looks like a mortarboard on top of a screen)
12. You should then be able to make queries and get a output of the top courses and their scores
