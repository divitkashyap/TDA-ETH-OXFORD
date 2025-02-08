import nltk 
import json

from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    sentiment = sia.polarity_scores(text)
    compound = sentiment["compound"]

    if compound >= 0.05:
        return "Positive 😊"
    elif compound <= -0.05:
        return "Negative 😡"
    else:
        return "Neutral 😐"
    

with open("tweets.txt","r",encoding="utf-8") as file1: 
    tweets = json.load(file1)
    print(tweets)
    for tweet in tweets:
        text = tweet["Tweet"]
        print(f"Tweet: {tweet} → Sentiment: {get_sentiment(tweet)}")

