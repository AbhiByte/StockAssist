#Import modules
import tweepy
from textblob import TextBlob

#Consumer keys
consumer_key = 'SECRET'
consumer_secret = 'SECRET'

#Access tokens
access_token = 'SECRET'
access_token_secret = 'SECRET'

#Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Main function to get tweets
def find_tweets(ticker_symbol):
    #Search for tweets with ticker symbol
    public_tweets = api.search(ticker_symbol)
    #Empy list for average of all sentiments
    sentiment_average_list = []

    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        sentiment_average_list.append(analysis.sentiment.polarity)

    return sentiment_average_list

#Calculates average sentiment
def average_sentiment(sentiment_average_list):
    #Returns average value
    return (sum(sentiment_average_list) / len(sentiment_average_list))


#Main code
ticker_symbol = str(input("Enter a stock's ticker symbol: "))
avg = average_sentiment(find_tweets(ticker_symbol.upper()))
print(avg)
