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
positiveLikeCount = 0
negativeLikeCount = 0
neutralLikeCount = 0

with open("tweets.json","r") as file1: 
    tweets = json.load(file1)
   
    for tweet in tweets:
        text = tweet["Tweet"]
        
        if tweet["Likes"] > 5000:
            influentialTweets.append(tweet)
       
        if (get_sentiment(text)) == "Negative 😡":
            negativeTweets.append ("@"+ tweet["Handle"]+ ": "+tweet["Tweet"])
            negativeLikeCount = negativeLikeCount + tweet["Likes"]
        if(get_sentiment(text)) == "Positive 😊":
            positiveTweets.append("@"+ tweet["Handle"]+ ": "+tweet["Tweet"])
            positiveLikeCount = positiveLikeCount + tweet["Likes"]
        else:
            neutralTweets.append("@"+ tweet["Handle"]+ ": "+tweet["Tweet"])
            neutralLikeCount = neutralLikeCount + tweet["Likes"]
        
        tokens = word_tokenize(text.lower())
        tokens = [word for word in tokens if word.isalnum()]  
        tokens = [word for word in tokens if word not in stop_words] 
        processed_docs.append(tokens)
        tagged = pos_tag(tokens)
        entityRec = ne_chunk(tagged)

with open('negativeTweets.txt', 'w') as negativeFile:
    for tweet in negativeTweets:
        negativeFile.write(tweet)

with open('positiveTweets.txt', 'w') as positiveFile:
    for tweet in positiveTweets:
        positiveFile.write(tweet)

with open('neutralTweets.txt', 'w') as neutralFile:
    for tweet in neutralTweets:
        neutralFile.write(tweet)
        
                
id2word = corpora.Dictionary(processed_docs)
corpus = [id2word.doc2bow(text) for text in processed_docs]


lda_model = LdaModel(corpus=corpus, id2word=id2word, num_topics=10, passes=10, random_state=42)
topics = lda_model.print_topics(num_words=10)


def displayPage():
    homepage = ("The top posts about crypto this week were from the following accounts" 
      + ", ".join([tweet["Handle"] for tweet in influentialTweets]))
    return homepage

def entityCount(file):
    with open(file,"r") as tweets:
        entities = []
        recurringEntities = []
        
        for tweet in tweets: 
            doc = nlp(tweet) 
        
        for ent in doc.ents:
            if ent.text == "#":
                continue 
            # elif ent.text.isdigit:
            #     continue
            else :
                entities.append(ent.text)
                recurringEntities.append(ent.text)

        returnThis = []
        
        for ent in entities:
            entCount = 0
        
            for ent2 in entities: 
                
                if not ent or not ent2 in recurringEntities:
                    if ent == ent2: 
                        entCount+=1
                
                entities.remove(ent)

            if entCount >= 2: 
                recurringEntities.append(ent)
                returnThis.append({"entity": ent, "appears": entCount})
                

    
    return returnThis



print(entityCount("positiveTweets.txt"))

        

