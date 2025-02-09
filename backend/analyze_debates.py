import nltk 
import os
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

def run_analysis():
    print("🔎 Running debate analysis...")

    # Your analysis logic here
    with open("tweets.json", "r") as file:
        tweets = json.load(file)
    
    # Process tweets and generate insights
    analysis_result = {"summary": "This is a sample analysis."}

    # Save analysis to a file
    with open("analysis.json", "w") as file:
        json.dump(analysis_result, file, indent=4)

    print("✅ Debate analysis completed.")

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

    with open("summary.txt","w") as summies:
        ranked_sentences = sorted(sentences, key=lambda s: sum(word_freq[word] for word in s.split()), reverse=True)
        summies.write(" ".join(ranked_sentences[:3]))
        # for tweet in tweets:
        #     if ranked_sentences[0] in tweet["Tweet"]:
        #         summies.write(tweet["Handle"]+ ": "+tweet["Tweet"]+"likes: "+str(tweet["Likes"])+"\n")
        #         break
        #     elif ranked_sentences[1] in tweet["Tweet"]:
        #         summies.write(tweet["Handle"]+ ": "+tweet["Tweet"]+"likes: "+str(tweet["Likes"])+"\n")
        #         break
        #     elif ranked_sentences[2] in tweet["Tweet"]:
        #         summies.write(tweet["Handle"]+ ": "+tweet["Tweet"]+"likes: "+str(tweet["Likes"])+"\n")
        #         break
        #     elif ranked_sentences[3] in tweet["Tweet"]:
        #         summies.write(tweet["Handle"]+ ": "+tweet["Tweet"]+"likes: "+str(tweet["Likes"])+"\n")
        #         break
        summies.close()

positiveLikeCount = 0
negativeLikeCount = 0
neutralLikeCount = 0


with open("tweets.json","r") as file1: 
    tweets = json.load(file1)
    extract_summary(tweets)
    for tweet in tweets:
        text = tweet["Tweet"]

        
        if tweet["Likes"] > 5000:
            print("adding inners\n")
            influentialTweets.append(tweet)
        
        if tweet["Followers"] > 10000:
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
   # Update displayPage() to save JSON instead of text
    with open("influential.json", "w") as file:
        json.dump(influentialTweets, file, indent=4)


import os
import matplotlib.pyplot as plt

def entityCount(file):
    with open(file, "r") as tweets:
        entities = []
        for tweet in tweets:
            doc = nlp(tweet)
            for ent in doc.ents:
                if ent.text == "#":
                    continue  
                entities.append(ent.text.lower())

    returnThis = Counter(entities)

    # ✅ Check if there are entities before saving
    if not returnThis:
        print(f"⚠ Warning: No entities found in {file}")
        return {}

    words, counts = zip(*returnThis.items())

    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.title(f"Frequency of Entities in {file}", fontsize=14)
    plt.xlabel("Entities", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # ✅ Remove ".txt" from filename before saving
    filename_without_ext = os.path.splitext(file)[0]  # Removes .txt
    output_filename = f"{filename_without_ext}.png"   # Adds .png

    plt.savefig(output_filename, format='png')
    print(f"✅ Saved plot as {output_filename}")  # Debugging log
    
    plt.close()

    return returnThis

    # ✅ Handle empty dictionary before unpacking
    if not returnThis:
        print(f"⚠ Warning: No entities found in {file}")
        return {}

    words, counts = zip(*returnThis.items())  # ✅ Fix unpacking issue

    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.title(f"Frequency of Entities in {file}", fontsize=14)
    plt.xlabel("Entities", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    filename_without_ext = os.path.splitext(file)[0]  # ✅ Removes ".txt"
    output_filename = filename_without_ext + ".png"   # ✅ Appends ".png"
    
    plt.savefig(output_filename, format='png')
    print(f"✅ Saved plot as {output_filename}")  # Debugging log
    
    plt.close()

    return returnThis
# with open("commonWords.txt", "w") as file: 
#     file.write("Positive words: " + entityCount("positiveTweets.txt"))
#     file.write("Negative words: " + entityCount("negativeTweets.txt").__str__)
#     file.write("Neutral words: " + entityCount("neutralTweets.txt").__str__)

# file.close()

displayPage()
entityCount("positiveTweets.txt")
entityCount("negativeTweets.txt")
entityCount("neutralTweets.txt")


        