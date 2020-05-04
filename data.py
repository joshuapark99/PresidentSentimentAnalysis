# Brian Park
import os
from dotenv import load_dotenv
load_dotenv()
from nltk.corpus import stopwords
import string
import twitter
from functools import partial
from sys import maxsize as maxint
import time
from urllib.error import URLError
from http.client import BadStatusLine
import json
import sys
from nltk import *
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tokenize import word_tokenize


states = {
    # 'Alabama': {
    #     'lat': 32.318230,
    #     'long': -86.902298,
    #     'radius': 85,
    # },
    # 'Alaska': {
    #     'lat': 	66.160507,
    #     'long': -153.369141,
    #     'radius': 700,
    # },
    # 'Arizona': {
    #     'lat': 34.048927,
    #     'long': -111.093735,
    #     'radius': 150,
    # },
    # 'Arkansas': {
    #     'lat': 34.799999,
    #     'long': -92.199997,
    #     'radius': 120,
    # },
    # 'Arkansas': {
    #     'lat': 34.048927,
    #     'long': -111.093735,
    #     'radius': 150,
    # },
    # 'California': {
    #     'lat': 36.778259,
    #     'long': -119.417931,
    #     'radius': 125,
    # },
    # 'Colorado': {
    #     'lat': 39.113014 ,
    #     'long': -105.358887,
    #     'radius': 140,
    # },
    # 'Connecticut': {
    #     'lat':41.599998,
    #     'long':-72.699997,
    #     'radius': 35,
    # },
    # 'Delaware': {
    #     'lat': 39.000000,
    #     'long':-75.500000,
    #     'radius': 4,
    # },
    # 'Florida': {
    #     'lat': 27.994402,
    #     'long': -81.760254,
    #     'radius': 130,
    # },
    # 'Georgia': {
    #     'lat': 33.247875,
    #     'long': -83.441162,
    #     'radius': 115,
    # },
    # 'Hawaii': {
    #     'lat': 19.741755,
    #     'long': -155.844437,
    #     'radius': 38,
    # },
    # 'Idaho': {
    #     'lat': 44.068203,
    #     'long': -114.742043,
    #     'radius': 152.5,
    # },
    # 'Illinois': {
    #     'lat': 40.000000,
    #     'long': -89.000000,
    #     'radius': 105,
    # },
    # 'Indiana': {
    #     'lat': 40.273502,
    #     'long': -86.126976,
    #     'radius': 120,
    # },
    # 'Iowa': {
    #     'lat': 42.032974 ,
    #     'long': -93.581543,
    #     'radius': 100,
    # },
    # 'Kansas': {
    #     'lat': 38.500000,
    #     'long': -98.000000,
    #     'radius': 105,
    # },
    # 'Kentucky': {
    #     'lat': 37.839333,
    #     'long': -84.270020,
    #     'radius': 120,
    # },
    # 'Louisiana': {
    #     'lat': 30.391830,
    #     'long': -92.329102,
    #     'radius': 115,
    # },
    # 'Maine': {
    #     'lat': 45.367584,
    #     'long': -68.972168,
    #     'radius': 105,
    # },
    # 'Maryland': {
    #     'lat': 39.045753,
    #     'long':-76.641273,
    #     'radius': 45,
    # },
    # 'Massachusetts': {
    #     'lat':42.407211,
    #     'long':-71.382439,
    #     'radius': 25,
    # },
    # 'Michigan': {
    #     'lat': 44.182205,
    #     'long': -84.506836,
    #     'radius': 120,
    # },
    # 'Minnesota': {
    #     'lat': 46.392410,
    #     'long': -94.636230,
    #     'radius': 175.5,
    # },
    # 'Mississippi': {
    #     'lat': 33.000000,
    #     'long': -90.000000,
    #     'radius': 135,
    # },
    # 'Missouri': {
    #     'lat': 38.573936,
    #     'long': -92.603760,
    #     'radius': 120,
    # },
    # 'Montana': {
    #     'lat': 46.965260,
    #     'long':-109.533691,
    #     'radius': 127.5,
    # },
    # 'Nebraska': {
    #     'lat': 41.500000,
    #     'long': -100.000000,
    #     'radius': 105,
    # },
    # 'Nevada': {
    #     'lat': 39.876019,
    #     'long': -117.224121,
    #     'radius': 160,
    # },
    # 'New Hampshire': {
    #     'lat': 44.000000,
    #     'long': -71.500000,
    #     'radius': 34,
    # },
    # 'New Jersey': {
    #     'lat': 39.833851,
    #     'long': -74.871826,
    #     'radius': 35,
    # },
    # 'New Mexico': {
    #     'lat': 34.307144,
    #     'long': -106.018066,
    #     'radius': 171.5,
    # },
    # 'New York': {
    #     'lat': 43.000000,
    #     'long': -75.000000,
    #     'radius': 141.5,
    # },
    # 'North Carolina': {
    #     'lat': 35.782169,
    #     'long': -80.793457,
    #     'radius': 75,
    # },
    # 'North Dakota': {
    #     'lat': 47.650589,
    #     'long': -100.437012,
    #     'radius': 100,
    # },
    # 'Ohio': {
    #     'lat': 40.367474,
    #     'long': -82.996216,
    #     'radius': 100,
    # },
    # 'Oklahoma': {
    #     'lat': 36.084621,
    #     'long': -96.921387,
    #     'radius': 110,
    # },
    # 'Oregon': {
    #     'lat': 44.000000,
    #     'long': -120.500000,
    #     'radius': 180,
    # },
    # 'Pennsylvania': {
    #     'lat': 41.203323,
    #     'long': -77.194527,
    #     'radius': 80,
    # },
    # 'Rhode Island': {
    #     'lat': 41.700001,
    #     'long': -71.500000,
    #     'radius': 10,
    # },
    # 'South Carolina': {
    #     'lat': 33.836082,
    #     'long': -81.163727,
    #     'radius': 100,
    # },
    # 'South Dakota': {
    #     'lat': 44.500000,
    #     'long': -100.000000,
    #     'radius': 100,
    # },
    # 'Tennessee': {
    #     'lat': 35.860119,
    #     'long': -86.660156,
    #     'radius': 60,
    # },
    # 'Texas': {
    #     'lat': 31.000000,
    #     'long': -100.000000,
    #     'radius': 320,
    # },
    # 'Utah': {
    #     'lat': 39.419220,
    #     'long': -111.950684,
    #     'radius': 130,
    # },
    # 'Vermont': {
    #     'lat': 44.000000,
    #     'long': -72.699997,
    #     'radius': 40,
    # },
    # 'Virginia': {
    #     'lat': 37.926868,
    #     'long': -78.024902,
    #     'radius': 100,
    # },
    # 'Washington': {
    #     'lat': 47.751076,
    #     'long': -120.740135,
    #     'radius': 120,
    # } ,
    # 'West Virginia': {
    #     'lat': 39.000000,
    #     'long': -80.500000,
    #     'radius': 60,
    # },
    # 'Wisconsin': {
    #     'lat': 44.500000,
    #     'long': -89.500000,
    #     'radius': 130,
    # },
    'Wyoming': {
        'lat': 43.075970,
        'long': -107.290283,
        'radius': 140,
    }
}


# cookbook function for api authentication
def oauth_login():
    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
    OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
    OAUTH_TOKEN_SECRET = os.getenv('OAUTH_TOKEN_SECRET')
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

# twitter cookbook function for creating a 
def make_twitter_request(twitter_api_func, max_errors=10, *args, **kw): 
    
    def handle_twitter_http_error(e, wait_period=2, sleep_when_rate_limited=True):
        
        if wait_period > 3600: # Seconds
            print('Too many retries. Quitting.', file=sys.stderr)
            raise e
    
        if e.e.code == 401:
            print('Encountered 401 Error (Not Authorized)', file=sys.stderr)
            return None
        elif e.e.code == 404:
            print('Encountered 404 Error (Not Found)', file=sys.stderr)
            return None
        elif e.e.code == 429: 
            print('Encountered 429 Error (Rate Limit Exceeded)', file=sys.stderr)
            if sleep_when_rate_limited:
                print("Retrying in 15 minutes...ZzZ...", f ile=sys.stderr)
                sys.stderr.flush()
                time.sleep(60*15 + 5)
                print('...ZzZ...Awake now and trying again.', file=sys.stderr)
                return 2
            else:
                raise e # Caller must handle the rate limiting issue
        elif e.e.code in (500, 502, 503, 504):
            print('Encountered {0} Error. Retrying in {1} seconds'.format(e.e.code, wait_period), file=sys.stderr)
            time.sleep(wait_period)
            wait_period *= 1.5
            return wait_period
        else:
            raise e

    
    wait_period = 2 
    error_count = 0 

    while True:
        try:
            return twitter_api_func(*args, **kw)
        except twitter.api.TwitterHTTPError as e:
            error_count = 0 
            wait_period = handle_twitter_http_error(e, wait_period)
            if wait_period is None:
                return
        except URLError as e:
            error_count += 1
            time.sleep(wait_period)
            wait_period *= 1.5
            print("URLError encountered. Continuing.", file=sys.stderr) 
            if error_count > max_errors:
                print("Too many consecutive errors...bailing out.", file=sys.stderr)
                raise
        except BadStatusLine as e:
            error_count += 1
            time.sleep(wait_period)
            wait_period *= 1.5
            print("BadStatusLine encountered. Continuing.", file=sys.stderr)
            if error_count > max_errors:
                print("Too many consecutive errors...bailing out.", file=sys.stderr)
                raise

def twitter_search(twitter_api, q, max_results=1000, state='Alabama', **kw):

    # initialize tweettokenizer, wordnetlemmatizer, stopwords
    tt = TweetTokenizer()
    wnl = WordNetLemmatizer()
    stop = stopwords.words('english')

    # initialize lat long and radius values
    lattitude = states[state]['lat']
    longitude = states[state]['long']
    radius = states[state]['radius']

    # make request with geocode values
    search_results = make_twitter_request(twitter_api.search.tweets, q=q, count=100,  geocode='{},{},{}mi'.format(lattitude, longitude, radius), tweet_mode='extended', **kw)
    statuses = search_results['statuses']

    count = 0
    output = []

    # iterate through first set of tweets 
    for tweet in search_results['statuses']:
            if 'retweeted_status' in tweet.keys():
                # get tweet's full text
                sample_tweet = tweet['retweeted_status']['full_text']
                # tokenize
                sample_tweet = tt.tokenize(sample_tweet)
                # lemmatize
                lemmatized = [wnl.lemmatize(t) for t in sample_tweet]
                # filter stopwords
                filtered = [w for w in lemmatized if w.lower() not in stop and w.lower() not in string.punctuation]
                filtered = " ".join(filtered)
                output.append(filtered)
            else:
                output.append(tweet['full_text'])

    # iterate through remaining tweets 100 at a time
    for i in range(max_results//100): 
        print(len(output))

        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError as e: # No more results when next_results doesn't exist
            break

        # get the next_results value            
        kwargs = dict([ kv.split('=') 
                        for kv in next_results[1:].split("&") ])
        
        # remove url encoded values
        kwargs['geocode'] = kwargs['geocode'].replace('%2C', ',')

        # make request with next_results value
        search_results = make_twitter_request(twitter_api.search.tweets, tweet_mode='extended', **kwargs)
        statuses += search_results['statuses']

        # iterate through tweets returned
        for tweet in search_results['statuses']:
            if 'retweeted_status' in tweet.keys():
                # get tweet's full text
                sample_tweet = tweet['retweeted_status']['full_text']
                # tokenize
                sample_tweet = tt.tokenize(sample_tweet)
                # lemmatize
                lemmatized = [wnl.lemmatize(t) for t in sample_tweet]
                # filter stopwords
                filtered = [w for w in lemmatized if w.lower() not in stop and w.lower() not in string.punctuation]
                filtered = " ".join(filtered)
                output.append(filtered)
            else:
                output.append(tweet['full_text'])

        # break out if no more tweets
        if len(statuses) > max_results: 
            break

    return output


# authenticate
twitter_api = oauth_login()
# initialize candidate
q = "trump"
num_results = 100

# iterate through each states
data = []
for state in states:
    # get all the tweets from the state
    results = twitter_search(twitter_api, q, max_results=num_results, state=state)
    # remove newline tags within tweet text
    results = [result.replace('\n', '') for result in results]
    # write all tweets to a text file
    with open('./output/{}{}.txt'.format(state, q), mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(results))



import glob
import requests
import csv

# read in list of all files for each state
files = glob.glob("output/*.txt")

# go through each file and make bulk request to sentiment140
for file in files:
    # make bulk request
    res = requests.post(url="http://www.sentiment140.com/api/bulkClassify?query={}?appid=jpark68@syr.edu".format(q),
        data=open(file, 'rb'))
    # output response to csv
    with open('output/{}{}.csv'.format(state, q),'wb') as file:
        file.write(res.text.encode(encoding='UTF-8'))
    

