import json

def extract_tweets(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    tweets = [entry["Tweet"] for entry in data if "Tweet" in entry and isinstance(entry["Tweet"], str) and entry["Tweet"].strip()]
    return tweets

with open('tweetsExtract.json', 'w') as extractedFile, open('tweets.json','r') as json_file:
    tweets = json.load(json_file)
    for tweet in tweets:
        tweetContent = tweet["Tweet"]
        extractedFile.write(tweetContent)
