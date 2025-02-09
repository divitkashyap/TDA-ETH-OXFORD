import requests
import json
import asyncio
import aiohttp
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST"], 
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
    {"prompt": "rugpull"},
    {"prompt": "blockchain"},
    {"prompt": "to the moon"},
    {"prompt": "mining"},
    {"prompt": "staking"},
    {"prompt": "DAO"},
    {"prompt": "defi"},
    {"prompt": "decentralized finance"},
    {"prompt": "lower transaction fees"}
]

headers = {
    "Authorization": "dt_$LSO2gvfJtB6UENHrgs-SS1w0zfSKmAr1gfkbBRmTkIg",  # ❗ Replace with your API key
    "Content-Type": "application/json"
}

async def fetch_tweets(session, payload):
    async with session.post(url, json=payload, headers=headers) as response:
        return await response.text()

async def process_payload(session, payload, file2, existing_ids, dictList):
    raw_data = await fetch_tweets(session, payload)
    data = json.loads(raw_data)
    
    new_tweets = []
    for tweet in data.get("miner_tweets", []):  # ✅ Use `.get()` to avoid KeyError
        if tweet["id"] not in existing_ids and tweet not in dictList:
            reformatted_tweet = {
                "Handle": tweet["user"]["username"],
                "Followers": tweet["user"]["followers_count"],
                "Likes": tweet["like_count"],
                "Retweets": tweet["retweet_count"],
                "Tweet": tweet["text"],
                "Date Posted": tweet["created_at"]
            }
            new_tweets.append(reformatted_tweet)
            file2.write(tweet["id"] + "\n")
    
    return new_tweets

async def main():
    dictList = []
    
    try:
        with open("tweetIds.txt", "r") as file2:
            existing_ids = set(file2.read().splitlines())
    except FileNotFoundError:
        existing_ids = set()
    
    async with aiohttp.ClientSession() as session:
        with open("tweets.json", "w") as file1, open("tweetIds.txt", "a") as file2:
            tasks = [process_payload(session, payload, file2, existing_ids, dictList) for payload in payloads]
            results = await asyncio.gather(*tasks)
            
            for new_tweets in results:
                dictList.extend(new_tweets)
            
            json.dump(dictList, file1)

    import analyze_debates  
    analyze_debates.run_analysis()  # ✅ Run analysis after fetching tweets
    print("✅ Tweets fetched & debates analyzed.")

# ✅ Run automatically when FastAPI starts
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(main())  # ✅ Runs asynchronously

@app.get("/tweets")
def get_tweets():
    try:
        with open("tweets.json", "r", encoding="utf-8") as file:
            return {"tweets": json.load(file)}
    except FileNotFoundError:
        return {"tweets": []}  
    
import os
from fastapi.staticfiles import StaticFiles

# Get the absolute path of the backend directory
backend_path = os.path.abspath(os.path.dirname(__file__))

# Mount the static folder
app.mount("/static", StaticFiles(directory=backend_path), name="static")

# ✅ API Endpoint to Fetch Summary
@app.get("/summary")
def get_summary():
    try:
        with open("summary.txt", "r") as file:
            summary = file.read().strip()
        return {"summary": summary}
    except FileNotFoundError:
        return {"summary": "No summary available yet."}

# ✅ API Endpoint to Fetch Plot URLs
@app.get("/plots")
def get_plots():
    return {
        "plot1": "/static/plot1.png",
        "plot2": "/static/plot2.png"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)