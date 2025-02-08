import os
import json
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Update with frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Now define your routes
@app.get("/tweets")
def get_tweets():
    with open("../tweets.json", "r", encoding="utf-8") as file:
        return {"tweets": json.load(file)}


TWEETS_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "tweets.json")
TWEET_IDS_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "tweetIds.txt")

# Function to fetch new tweets
def fetch_new_tweets():
    url = "https://apis.datura.ai/desearch/ai/search/links/twitter"
    payloads = [{"prompt": "arguments in crypto"}, {"prompt": "crypto good"}, {"prompt": "crypto bad"}]

    headers = {
        "Authorization": "your_api_key_here",
        "Content-Type": "application/json"
    }

    # Read existing tweet IDs to prevent duplicates
    with open(TWEET_IDS_FILE_PATH, "a+") as file2:
        file2.seek(0)  # Move cursor to start before reading
        ids = file2.read().splitlines()  # Read as a list of IDs

    tweet_list = []

    for payload in payloads:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()

            for tweet in data.get("miner_tweets", []):
                if tweet["id"] not in ids:
                    formatted_tweet = {
                        "Handle": tweet["user"]["username"],
                        "Followers": tweet["user"]["followers_count"],
                        "Likes": tweet["like_count"],
                        "Retweets": tweet["retweet_count"],
                        "Tweet": tweet["text"],
                        "Date Posted": tweet["created_at"]
                    }
                    tweet_list.append(formatted_tweet)
                    file2.write(tweet["id"] + "\n")  # Save new tweet ID

    # Save tweets to JSON file
    with open(TWEETS_FILE_PATH, "w", encoding="utf-8") as file1:
        json.dump(tweet_list, file1, indent=4)

# Load JSON file function
def load_tweets():
    try:
        with open(TWEETS_FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"error": "tweets.json not found or invalid JSON format"}

# API Routes
@app.get("/tweets")
def get_tweets():
    return {"tweets": load_tweets()}

@app.post("/fetch-new-tweets")
def update_tweets():
    fetch_new_tweets()
    return {"message": "Tweets updated successfully"}