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

nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))

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
with open("tweets.json","r") as file1, open("sentiment.json","a+") as file2: 
    tweets = json.load(file1)
    for tweet in tweets:
        text = tweet["Tweet"]
        tokens = word_tokenize(text.lower())
        tokens = [word for word in tokens if word.isalnum()]  # Remove punctuation
        tokens = [word for word in tokens if word not in stop_words] 
        processed_docs.append(tokens)
        tagged = pos_tag(tokens)
        entityRec = ne_chunk(tagged)
        file2.write(f"Tweet: {text} → Sentiment: {get_sentiment(text)}\n")
        doc = nlp(text)
        for ent in doc.ents:
            print(f"Entity: {ent.text}, Label: {ent.label_}")
        
                
id2word = corpora.Dictionary(processed_docs)
corpus = [id2word.doc2bow(text) for text in processed_docs]

#print(corpus)
# Train LDA model
lda_model = LdaModel(corpus=corpus, id2word=id2word, num_topics=10, passes=10, random_state=42)

# Print the topics
topics = lda_model.print_topics(num_words=5)
for topic in topics:
    print(topic)