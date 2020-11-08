import spacy
import nltk
from nltk.corpus import stopwords
import re

#loading pre-define language model from english
nlp = spacy.load('en_core_web_sm')

#tagger, parser and ner
nlp.pipe_names

# Creating random text so the pre-built model can identify entities within text
text = "Robert does not like fish with bones. He is from Shanghai."

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)

#================================================================
#https://fairyonice.github.io/extract-someones-tweet-using-tweepy.html
import time
import webbrowser
import tweepy



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
redirect_url = auth.get_authorization_url()
print(redirect_url)

user_pin = '8076197'
auth.get_access_token(user_pin)


api = tweepy.API(auth)

tweets = []
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, time_limit=1):
        self.start_time = time.time()
        self.limit = time_limit
        super(MyStreamListener, self).__init__()

    def on_status(self, status):
        tweets.append(status.text)

        if (time.time() - self.start_time) < self.limit:
            return True
        else:
            return False

myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener(time_limit=30))
myStream.filter(track=['Donald Trump'])

tweets
#tweets.append('RT @jocmitchell11: For reference https://t.co/aMzQgn9F91')
#'RT @jocmitchell11: For reference https://t.co/aMzQgn9F91'

def preprocess(tweets):

    for tweet in range(len(tweets)): 
    
        letters_only_text = re.sub(r"https:(\/\/t\.co\/([A-Za-z0-9]|[A-Za-z]){10})", '', tweets[tweet], flags=re.MULTILINE)

        # keep only words
        letters_only_text = re.sub(r'[^a-zA-Z\s]', " ", letters_only_text)
        #r'https?:\/\/\S*', '', text
        # Remove urls
        #letters_only_text = re.sub(r"http\S+|www\S+|https\S+", '', letters_only_text, flags=re.MULTILINE)

        # convert to lower case and split 
        words = letters_only_text.lower().split()
        
        # remove stopwords
        #stopword_set = set(stopwords.words("english"))
        additional  = ['rt','rts','retweet']
        stopword_set = set().union(stopwords.words('english'),additional)
        meaningful_words = [w for w in words if w not in stopword_set]
        
        # join the cleaned words in a list
        tweets[tweet] = " ".join(meaningful_words)

    return tweets


preprocess(tweets)

tweets

entity_labels = []

for tweet in range(len(tweets)): 

    doc = nlp(tweets[tweet])
    for ent in doc.ents:
        print(ent.text, ent.label_)
        if not ent.label_ in entity_labels:
            entity_labels.append(ent.label_)


    
    
    