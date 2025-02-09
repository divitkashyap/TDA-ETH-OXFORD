import requests
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline

app = FastAPI()  

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_with_bart(tweets, max_length=150, min_length=50):
    """
    Summarize tweets using BART model with chunking for long texts
    """
    full_text = " ".join([tweet["Tweet"] for tweet in tweets])
    
    # BART has 1024 token limit - split into chunks
    chunk_size = 1000  # Characters (safe margin)
    chunks = [full_text[i:i+chunk_size] for i in range(0, len(full_text), chunk_size)]
    
    summaries = []
    for chunk in chunks:
        summary = summarizer(
            chunk,
            max_length=max_length,
            min_length=min_length,
            do_sample=False,
            truncation=True
        )[0]['summary_text']
        summaries.append(summary)
    
    # Combine chunk summaries and summarize final
    combined = " ".join(summaries)
    return summarizer(
        combined,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )[0]['summary_text']

def extract_summary(tweets):
    # First get most frequent debate topic
    frequent_words = get_most_frequent_debate_words(tweets)
    if not frequent_words:
        return "No clear debate topics identified"
    
    main_topic = frequent_words[0][0]
    
    # Filter tweets containing main topic
    topic_tweets = [
        t for t in tweets 
        if main_topic.lower() in t["Tweet"].lower()
    ]
    
    # Generate BART summary focused on main topic
    return f"🔥 Main Debate Topic: {main_topic.upper()}\n" + \
           summarize_with_bart(topic_tweets)

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
    
@app.get("/tweets")
def get_tweets():
    try:
        with open("tweets.json", "r", encoding="utf-8") as file:
            tweets = json.load(file)
            return {
                "tweets": tweets,
                "debate_summary": extract_summary(tweets),
                "main_topic": get_most_frequent_debate_words(tweets)[0][0] if get_most_frequent_debate_words(tweets) else None
            }
    except FileNotFoundError:
        return {"tweets": [], "debate_summary": "No debate data available"}


if __name__ == "__main__":
    import uvicorn
    fetch_tweets() 
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

