import requests
import json
url = "https://apis.datura.ai/twitter"

payload = {
    "query": "crypto",
    "sort": "Top",
    "lang": "en",
     "min_likes": 2000,
            }
headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

rawData =response.text
data = json.loads(rawData)

for tweet in data:
    print("Twitter handle: " + tweet["user"]["username"])
    print("Followers: " + tweet["user"]["followers_count"])
   # print("Likes: "+ tweet["like_count"])
    #print("Views: "+ tweet["view_count"])
   # print("Retweets: "+ tweet["retweet_count"])
    print("Tweet: " + tweet["text"] + "\nEND OF TWEET\n")

    print("\n")



