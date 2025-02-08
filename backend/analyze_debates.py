import nltk 
import json
import spacy 
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import word_tokenize, pos_tag, ne_chunk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')

try:
    nltk.data.find('chunkers/maxent_ne_chunker')
except LookupError:
    nltk.download('maxent_ne_chunker')

try:
    nltk.data.find('corpora/words')
except LookupError:
    nltk.download('words')

sia = SentimentIntensityAnalyzer()
nlp = spacy.load("en_core_web_sm")

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
        doc = nlp(text)
        for ent in doc.ents:
            print(f"Entity: {ent.text}, Label: {ent.label_}")
                

