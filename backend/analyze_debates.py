import nltk 
import json
import spacy 
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import word_tokenize, pos_tag, ne_chunk
import gensim
import gensim.corpora as corpora
from gensim.models.ldamodel import LdaModel
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

nltk.download("vader_lexicon")
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))

crypto_dict = {
    "Bitcoin": "BTC",
    "Ethereum": "ETH",
    "Solana": "SOL",
    "Ripple": "XRP",
    "Dogecoin": "DOGE",
    "Cardano": "ADA",
    "Polkadot": "DOT",
    "Chainlink": "LINK"
}

country_abbreviations = {
    "United States": ["USA", "U.S.", "America", "United States of America"],
    "United Kingdom": ["UK", "U.K.", "Britain", "England", "Great Britain"]
}

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

processed_docs = []
influentialTweets = []
negativeTweets = []
positiveTweets = []
neutralTweets = []
entities = []

with open("tweets.json","r") as file1, open("sentiment.json","w+") as file2: 
    tweets = json.load(file1)
   
    for tweet in tweets:
        text = tweet["Tweet"]
        
        if tweet["Likes"] > 5000:
            influentialTweets.append(tweet)
       
        if (get_sentiment(text)) == "Negative 😡":
            negativeTweets.append ("@"+ tweet["Handle"]+ ": "+tweet["Tweet"])
        if(get_sentiment(text)) == "Positive 😊":
            positiveTweets.append("@"+ tweet["Handle"]+ ": "+tweet["Tweet"])
        else:
            neutralTweets.append("@"+ tweet["Handle"]+ ": "+tweet["Tweet"])
        
        tokens = word_tokenize(text.lower())
        tokens = [word for word in tokens if word.isalnum()]  
        tokens = [word for word in tokens if word not in stop_words] 
        processed_docs.append(tokens)
        tagged = pos_tag(tokens)
        entityRec = ne_chunk(tagged)

        file2.write(f"Tweet: {text} → Sentiment: {get_sentiment(text)}\n\n")
        
        doc = nlp(text) 

with open('negativeTweets.txt', 'w') as negativeFile:
    for tweet in negativeTweets:
        negativeFile.write(tweet)

with open('positiveTweets.txt', 'w') as positiveFile:
    for tweet in positiveFile:
        positiveFile.write(tweet)

with open('neutralTweets.txt', 'w') as neutralFile:
    for tweet in neutralFile:
        neutralFile.write(tweet)


    for ent in doc.ents:
        entities.append(ent.text.lower())
        
                
id2word = corpora.Dictionary(processed_docs)
corpus = [id2word.doc2bow(text) for text in processed_docs]


#print(corpus)

lda_model = LdaModel(corpus=corpus, id2word=id2word, num_topics=10, passes=10, random_state=42)
topics = lda_model.print_topics(num_words=10)


def displayPage():
    homepage = ("The top posts about crypto this week were from the following accounts" 
      + ", ".join([tweet["Handle"] for tweet in influentialTweets]))
    return homepage

def entityCount():
    recurringEntities = []
    returnThis = []
    count = []
    for ent in entities:
        entCount = 0
        
        for ent2 in entities: 
            
            if not ent or not ent2 in recurringEntities:
                if ent == ent2: 
                    entCount+=1

        if entCount >= 2: 
            recurringEntities.append(ent)
            count.append(entCount)
            returnThis.append({"entity": ent, "appears": entCount})
            entities.remove(ent)

    
    return returnThis



print(entityCount())

        

