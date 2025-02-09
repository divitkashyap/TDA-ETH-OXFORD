import requests
import json
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
    {"prompt": "rugged"},
    {"prompt": "blockchain"},
    {"prompt": "to the moon"},
    {"prompt": "mining"},
    {"prompt": "staking"},
    {"prompt": "DAO"},
    {"prompt": "defi"},
    {"prompt": "decentralized finance"},
    {"prompt": "apeing"},
    {"prompt": "lower transaction fees"}
]

headers = {
    "Authorization": "dt_$LSO2gvfJtB6UENHrgs-SS1w0zfSKmAr1gfkbBRmTkIg",
    "Content-Type": "application/json"
}

def fetch_tweets():
    dict_list = []
    with open("tweets.json", "w") as file1, open("tweetIds.txt", "r+") as file2:
        for payload in payloads:
            response = requests.post(url, json=payload, headers=headers)
             
            data = response.json()

            ids = file2.read()
            file2.seek(0,2)

            for tweet in data.get("miner_tweets", []): 
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

@app.on_event("startup")
async def startup_event():
    fetch_tweets()
    await asyncio.to_thread(analyze_tweets)  # ✅ Run `analyze_tweets.py` in a non-blocking way
    print("✅ Tweets fetched & debates analyzed.")


@app.get("/tweets")
def get_tweets():
    try:
        with open("tweets.json", "r", encoding="utf-8") as file:
            return {"tweets": json.load(file)}
    except FileNotFoundError:
        return {"tweets": []}  



if __name__ == "__main__":
    import uvicorn
    fetch_tweets() 
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

