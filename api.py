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
with open("tweets.txt","a+") as file1, open("ids.txt","a+") as file2:
    ids = file2.read()
    for tweet in data:
        if (tweet["id"] not in ids):
            file1.write("Handle: "+ tweet["user"]["username"]+"\n")
            file1.write("Followers: %d" %tweet["user"]["followers_count"]+"\n")
            file1.write("Likes: %d" %tweet["like_count"]+"\n")
            file1.write("Retweets: %d" %tweet["retweet_count"]+"\n")
            file1.write("Tweet: " + tweet["text"]+"\n"+"\n")
            file1.write("Date Posted: "+ tweet["created_at"])
            file2.write(tweet["id"]+"\n")
        else:
            print("Already have tweet\n")
    file1.close()