#Import modules
import tweepy
from textblob import TextBlob
import asyncio
import discord
from discord.ext import commands


#Consumer keys
consumer_key = '9Nmb522FbZ8Q5GEDkucdFTuTz'
consumer_secret = 'RFuTgmanJGKzhhm5WsLAuOQqHVEO0M4WfKJZEeMUXJ8KDZDF7D'

#Access tokens
access_token = '2281365362-aGw4Zakc0abIZqfSZl1j3D78xYyPRofiOCRRPPh'
access_token_secret = 'csVekppWm9neGGMEkCRZUDmfVQJc4vyoZ6ABzzDLSPUVX'

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
    average = (sum(sentiment_average_list) / len(sentiment_average_list))
    return average
async def f_t_test(ctx):
    find_tweets()
    await ctx.send(sentiment_average_list)
async def a_s_test(ctx):
    average_sentiment()
    await ctx.send(average)
#Main code
def runner_code():
    ticker_symbol = str(input("Enter a stock's ticker symbol: "))
    avg = average_sentiment(find_tweets(ticker_symbol.upper()))
    print(f'The average sentiment for your stock (-1 to +1, -1 being very negative and +1 being very positive) on Twitter right now is {round(avg, 3)}')

runner_code()
