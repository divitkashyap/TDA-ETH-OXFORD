import requests
import json
#url = "https://apis.datura.ai/twitter"

#payload = {
    #"query": "crypto",
    #"sort": "Top",
    #"lang": "en",
   #  "min_likes": 200,
 #           }
#headers = {
 #   "Authorization": "REMOVED",
  #  "Content-Type": "application/json"
#
url = "https://apis.datura.ai/desearch/ai/search/links/twitter"

payloads = [{"prompt": "arguments in crypto"},
            {"prompt": "crypto good"},
            {"prompt": "crypto bad"},
            {"prompt": "future of crypto"}]

headers = {
    "Authorization": "REMOVED",
    "Content-Type": "application/json"
}

# rawData = (requests.request("POST", url, json={"prompt": "crypto"}, headers=headers)).text
dictList = []
with open("tweets.json","w+") as file1, open("tweetIds.txt","w+") as file2:
    for payload in payloads: 
        response = requests.request("POST", url, json=payload, headers=headers)
        rawData = response.text  

        data = json.loads(rawData)

        
        ids = file2.read()
       
        for tweet in data["miner_tweets"]:
            if (tweet["id"] not in ids and tweet not in dictList):
                reformatedTweet = {
                            "Handle": tweet["user"]["username"], 
                            "Followers":tweet["user"]["followers_count"],
                            "Likes":tweet["like_count"],
                            "Retweets": tweet["retweet_count"],
                            "Tweet": tweet["text"],
                            "Date Posted": tweet["created_at"]
                            }
                dictList.append(reformatedTweet)
                file2.write(tweet["id"]+"\n")
            else:
                print("Already have tweet\n")
                

    json.dump(dictList,file1,indent =4 )
file1.close()
file2.close()