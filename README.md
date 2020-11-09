# Twitter-Text-Analysis

https://github.com/JaimeGoB/Twitter-Text-Analysis/blob/main/README.md

# How to run the program:

This program can be run one cell at a time. However, there are some variables to must be overwritten before you can run the rest of the program

**Before running the entire program these variables in bold must be overwritten.**


## Setting up API Variables

#Consume:

**CONSUMER_KEY    = ''**

**CONSUMER_SECRET = ''**

#Access:

**ACCESS_TOKEN  = ''**

**ACCESS_SECRET = ''**

## Authenticating - Getting User-pin

#PIN provided by API

**user_pin = ''**

auth.get_access_token(user_pin)

Once these variables have been properly overwritten you can run the entire program once cell at a time.

# Flow Diagram

<img src="https://github.com/JaimeGoB/Twitter-Text-Analysis/blob/main/data/sequence_diagram.png" length = 1000 width="600"/>

# Tweets

## Raw Tweets

<img src="https://github.com/JaimeGoB/Twitter-Text-Analysis/blob/main/data/raw_tweets.png" length = 1000 width="600"/>

## Preprocessed Tweets

<img src="https://github.com/JaimeGoB/Twitter-Text-Analysis/blob/main/data/processed_tweets.png"/>

# Results

## Date - Label for different time intervals

<img src="https://github.com/JaimeGoB/Twitter-Text-Analysis/blob/main/data/date.png" length = 1000 width="600"/>


## Different Class Labels, Entity recognized from tweet and count of entity after 10 minute time interval 
<img src="https://github.com/JaimeGoB/Twitter-Text-Analysis/blob/main/data/10min.png" length = 1000 width="600"/>
