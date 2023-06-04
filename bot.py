import tweepy
import config

# Twitter API credentials
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret


# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Define the search query
query = "What is a woman?"

# Retrieve tweets with over a million likes
tweets = api.search_tweets(q=query, lang="en", tweet_mode='extended')

# Retweet each of the tweets
for tweet in tweets:
    if tweet.favorite_count > 1000000:
        print(f"{tweet.user.name}:{tweet.text}")
        api.retweet(tweet.id)
