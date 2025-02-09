import requests
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  # ✅ Define the FastAPI app

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (replace with ["http://localhost:5173"] for security)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


url = "https://apis.datura.ai/desearch/ai/search/links/twitter"

payloads = [
    {"prompt": "arguments in crypto"},
    {"prompt": "crypto good"},
    {"prompt": "crypto bad"},
    {"prompt": "future of crypto"},
    {"prompt": "crypto"},
    {"prompt": "pump and dump"},
    {"prompt": "rug pull"},
]

headers = {
    "Authorization": "dt_$LSO2gvfJtB6UENHrgs-SS1w0zfSKmAr1gfkbBRmTkIg",
    "Content-Type": "application/json"
}

def fetch_tweets():
    dict_list = []
    with open("tweets.json", "w") as file1, open("tweetIds.txt", "w+") as file2:
        for payload in payloads:
            response = requests.post(url, json=payload, headers=headers)
            data = response.json()

            ids = file2.read()

            for tweet in data.get("miner_tweets", []):  # ✅ Prevent KeyError
                if tweet["id"] not in ids and tweet not in dict_list:
                    reformatted_tweet = {
                        "Handle": tweet["user"]["username"],
                        "Followers": tweet["user"]["followers_count"],
                        "Likes": tweet["like_count"],
                        "Retweets": tweet["retweet_count"],
                        "Tweet": tweet["text"],
                        "Date Posted": tweet["created_at"],
                    }
                    dict_list.append(reformatted_tweet)
                    file2.write(tweet["id"] + "\n")
                else:
                    print("Already have tweet\n")


        json.dump(dict_list, file1, indent=4)


# ✅ API Route for Frontend
@app.get("/tweets")
def get_tweets():
    try:
        with open("tweets.json", "r", encoding="utf-8") as file:
            return {"tweets": json.load(file)}
    except FileNotFoundError:
        return {"tweets": []}  # Return empty list if file doesn't exist



if __name__ == "__main__":
    import uvicorn
    fetch_tweets()  # ✅ Fetch tweets before starting API
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

