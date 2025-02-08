import requests
import json

url = "https://apis.datura.ai/desearch/ai/search/links/twitter"

payloads = [{"prompt": "arguments in crypto"},
            {"prompt": "crypto good"},
            {"prompt": "crypto bad"},
            {"prompt": "future of crypto"},
            {"prompt": "crypto"},
            {"prompt": "pump and dump" },
            {"prompt": "rug pull"},
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
            {"prompt": "lower transaction fees"},
            ]

headers = {
    "Authorization": "REMOVED",
    "Content-Type": "application/json"
}

# rawData = (requests.request("POST", url, json={"prompt": "crypto"}, headers=headers)).text
import asyncio
import aiohttp
import json

async def fetch_tweets(session, payload):
    async with session.post(url, json=payload, headers=headers) as response:
        return await response.text()

async def process_payload(session, payload, file2, existing_ids, dictList):
    raw_data = await fetch_tweets(session, payload)
    data = json.loads(raw_data)
    
    new_tweets = []
    for tweet in data["miner_tweets"]:
        if tweet["id"] not in existing_ids and tweet not in dictList:
            reformated_tweet = {
                "Handle": tweet["user"]["username"],
                "Followers": tweet["user"]["followers_count"],
                "Likes": tweet["like_count"],
                "Retweets": tweet["retweet_count"],
                "Tweet": tweet["text"],
                "Date Posted": tweet["created_at"]
            }
            new_tweets.append(reformated_tweet)
            file2.write(tweet["id"] + "\n")
        else:
            print("Already have tweet")
    return new_tweets

async def main():
    dictList = []
    
    # Read existing IDs first
    with open("tweetIds.txt", "r+") as file2:
        existing_ids = set(file2.read().splitlines())
    
    async with aiohttp.ClientSession() as session:
        with open("tweets.json", "w+") as file1, open("tweetIds.txt", "a") as file2:
            # Create tasks for all payloads
            tasks = [
                process_payload(session, payload, file2, existing_ids, dictList)
                for payload in payloads
            ]
            
            # Wait for all tasks to complete
            results = await asyncio.gather(*tasks)
            
            # Flatten results and extend dictList
            for new_tweets in results:
                dictList.extend(new_tweets)
            
            # Write to JSON file
            json.dump(dictList, file1)

# Run the async code
asyncio.run(main())