import nltk 
import json

from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import word_tokenize, pos_tag, ne_chunk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
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
    

with open("tweets.json","r") as file1: 
    tweets = json.load(file1)
    for tweet in tweets:
        text = tweet["Tweet"]
        tokens = word_tokenize(text)
        tagged = pos_tag(tokens)
        entityRec = ne_chunk(tagged)
        print(f"Tweet: {text} → Sentiment: {get_sentiment(text)}")
       
        
                

