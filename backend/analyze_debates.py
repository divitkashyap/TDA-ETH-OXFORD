import nltk 
import json
import spacy 
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from collections import Counter

nltk.download("vader_lexicon")
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
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
numNeutral = 0 
numPositive = 0 
numNegative = 0 

def extract_summary(tweets):
    text = " ".join([tweet["Tweet"] for tweet in tweets])
    sentences = sent_tokenize(text)
    
   
    words = nltk.word_tokenize(text.lower())
    word_freq = Counter(words)

   
    ranked_sentences = sorted(sentences, key=lambda s: sum(word_freq[word] for word in s.split()), reverse=True)
    
    with open("summary.txt","w") as summies:
        summies.write(" ".join(ranked_sentences[:3]))
    


positiveLikeCount = 0
negativeLikeCount = 0
neutralLikeCount = 0


with open("backend/tweets.json","r") as file1: 
    tweets = json.load(file1)
    for tweet in tweets:
        text = tweet["Tweet"]

        
        if tweet["Likes"] > 5000:
            influentialTweets.append(tweet)
       
        if (get_sentiment(text)) == "Negative 😡":
            negativeTweets.append ("@"+ tweet["Handle"]+ ": "+tweet["Tweet"])
            numNegative+=1
            negativeLikeCount = negativeLikeCount + tweet["Likes"]

        if(get_sentiment(text)) == "Positive 😊":
            positiveTweets.append("@"+ tweet["Handle"]+ ": "+tweet["Tweet"])
            numPositive+=1
            positiveLikeCount = positiveLikeCount + tweet["Likes"]
        else:
            neutralTweets.append("@"+ tweet["Handle"]+ ": "+tweet["Tweet"])
            neutralLikeCount = neutralLikeCount + tweet["Likes"]
            numNeutral+=1
        
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
        
                
# id2word = corpora.Dictionary(processed_docs)
# corpus = [id2word.doc2bow(text) for text in processed_docs]


# lda_model = LdaModel(corpus=corpus, id2word=id2word, num_topics=10, passes=10, random_state=42)
# topics = lda_model.print_topics(num_words=10)

import matplotlib.pyplot as plt

labels = ['Positive', 'Negative', 'Neutral']
sizes = [numPositive, numNegative, numNeutral]
colors = ['green', 'red', 'gray']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.axis('equal')
plt.title("Crypto Twitter Sentiment Breakdown")
plt.savefig('plot1.png',format = 'png')
plt.close()


labels1 = ['Positive Likes', 'Negative Likes', 'Neutral Likes']
sizes1 = [positiveLikeCount, negativeLikeCount, neutralLikeCount]
plt.pie(sizes1, labels=labels1, autopct='%1.1f%%', colors=colors, startangle=140)
plt.axis('equal')
plt.title("What the people are liking")
plt.savefig('plot2.png',format = 'png')
plt.close()


def displayPage():
    with open("influential.txt","w") as inners:
        for tweet in influentialTweets:
            inners.write[tweet.text]     
    inners.close()


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
                isCountry = False
                isCoin = False
                for country, aliases in country_abbreviations.items():
                    for alias in aliases: 
                        if ent.text in alias.lower():
                            entities.append(country.lower())
                            
                            isCountry = True

                for name, ticket in crypto_dict.items():
                    if ent.text in ticket.lower():
                        entities.append(name.lower())
                        
                        isCoin = True

                if isCoin == False and isCountry == False: 
                    
                    entities.append(ent.text.lower())
                    recurringEntities.append(ent.text.lower())
        returnThis = Counter(entities)
    
    return returnThis


displayPage()

print(entityCount("backend/negativeTweets.txt"))



        

