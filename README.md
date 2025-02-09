# Twitter Debate Analyser 

## Description 
This project entails creating a bot that analyses debates about crypto on X (formerly known as Twitter). Here is the outline of the bounty as described on the ETH Torus Github: 
- Analysis tool that identifies debates and conflicts between influential Crypto Twitter accounts
- Measuring issue importance, influence of involved accounts, and stance of participants
- Generates detailed summaries of debates including main points, arguments of both sides, and underlying narratives
- Provides clear info about debate participants on each side and their positions
- Detect underlying real-world events that may have triggered/influenced the debate, that are inferrable from the debate content

Here is the link to the full set of instructions: https://gist.github.com/Boscop/f11cba6094ddcd87ab871de501a453e3#-ideal-project-1

## Our Project
We managed to set up the beginnings of a very good Debate Analyzer by collecting as many relevant tweets as we could using the APi and then processing them through various Natrual Language Processing techniques and libraries. In the end, we had too much data to collate and ended up not being able to use some of the most influential data. As a result, we are left with a very bare bones, but still some what functional crypto tweet analyser. 

## Building it on Your Own Device
At the moment, you would have to run git clone https://github.com/divitkashyap/TDA-ETH-OXFORD to access our repository. The dockerfile will be functional shortly. After cloninhg the repository, make sure that you have activated a python virtual environment, like conda activate or source myenv/bin/activate should work as we have avirtial environment that should have all of the different libraries and packages needed for this project (which are plentiful). After activating the environment navigate to backend/ (cd backend) and "run uvicorn fetch_tweets:app --reload". Now, you should see the server being started and the backend should run some calculations (might take a while to import all the libraries as well). Open another terminal and navigate to frontend/ and run the following command " npm run dev". You should now see a localhost:xxxx where xxxx will be some port number. Paste that into a browser and you should be seeing our frontend!!!
