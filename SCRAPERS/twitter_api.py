from ast import keyword
import tweepy
import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_secret_key = config['twitter']['api_secret_key']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

keywords = '#grossesse'
limit = 300

tweets = tweepy.Cursor(api.search_tweets, q = keywords, count = 100, tweet_mode = 'extended').items(limit)

columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)
df.to_csv('tweets_api.csv', index=False)

print(df)
