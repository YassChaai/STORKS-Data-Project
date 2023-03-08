import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "#futuremaman"
tweets = []
limits = None

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limits:
        break
    else:
        tweets.append([tweet.date, tweet.id, tweet.content])

df = pd.DataFrame(tweets, columns=['Datetime', 'Tweet Id', 'Content'])
df.to_csv('tweets_3.csv', index=False)