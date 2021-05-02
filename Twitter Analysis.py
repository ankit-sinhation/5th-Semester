# installing  twitter module
#!pip  install tweepy
import tweepy
#  defining variables
#  consumer keys from twitter
consumer_key="enter your consumer key"
consumer_sec="enter your consumer security key"
# authentication tokens
first_auth=tweepy.OAuthHandler(consumer_key,consumer_sec)
access_key="enter your access key"
access_sec="enter your security access key"
first_auth.set_access_token(access_key,access_sec)
#  pointing  auth to datastore
storage_api_connect=tweepy.API(first_auth,timeout=2)
# input the word to search
search_data=["hero"]
list_of_tweets=[] # tweet data store
if  len(search_data) == 1 : 
  for  tweetdata  in  tweepy.Cursor(storage_api_connect.search,q=search_data[0]+"  -filter:retweets",lang='en',result_type='recent').items(5):
    list_of_tweets.append(tweetdata.text)
    #print(tweetdata.text)    
#print(" ")
#for i in range(1,len(list_of_tweets)):
#  print("Tweet",i,": ",list_of_tweets[i-1])

from textblob  import  TextBlob   #  automated way of sentiment analysis 
search_sentiment=["hero"]  #  search list
list_of_sentiment=[]   #  sentiment data store
z=1 # count purpose
if  len(search_sentiment) >= 1 : 
  for  i  in  tweepy.Cursor(storage_api_connect.search,q=search_sentiment[0]+"  -filter:retweets",lang='en',result_type='recent').items(5):
    analyse=TextBlob(i.text)
    print("Tweet",z,": ",list_of_tweets[z-1])
    print("Its sentiment polarity:",analyse.sentiment.polarity)
    z=z+1
    print(" ")
    #print(i.text)
