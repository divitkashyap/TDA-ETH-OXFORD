import requests
import json
url = "https://apis.datura.ai/twitter"

payload = {
    "query": "crypto",
    "sort": "Top",
    "lang": "en",
     "min_likes": 200,
            }
headers = {
    "Authorization": "dt_$LSO2gvfJtB6UENHrgs-SS1w0zfSKmAr1gfkbBRmTkIg",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

rawData =response.text
data = json.loads(rawData)
with open("tweets.json","a+") as file1, open("ids.txt","w+") as file2:
    ids = file2.read()
    for tweet in data:
        if (tweet["id"] not in ids):
            reformatedTweet = {"Handle": tweet["user"]["username"], 
                    "Followers":tweet["user"]["followers_count"],
                    "Likes":tweet["like_count"],
                     "Retweets": tweet["retweet_count"],
                     "Tweet": tweet["text"],
                     "Date Posted": tweet["created_at"]
                     }
            json.dump(reformatedTweet,file1,indent =1 )
            file2.write(tweet["id"]+"\n")
        else:
            print("Already have tweet\n")
    file1.close()