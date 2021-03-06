
!pip install python-twitter

!pip install paralleldots

!pip install tweepy

!pip install nltk


import twitter
api = twitter.Api(consumer_key = '',

                  		consumer_secret = '',
                  
				access_token_key = '',
                  
				access_token_secret = '')


API_KEY = ''

API_SECRET = ''

ACCESS_TOKEN = ''

ACCESS_TOKEN_SECRET = ''



def get_status(query):
  
import pprint
  
hasgtag = "#" + query
  
tweets = api.GetSearch(hasgtag , count=10 , return_json=True)
  
pp = pprint.PrettyPrinter(indent=2)
  
pp.pprint(tweets)



def get_tweets(query):
  
hashtag = "#" + query
  
tweets = api.GetSearch(hashtag , count=10 , return_json=True)
  
return tweets



def get_analyse(query):
  
tweets = get_tweets(query)
  
import paralleldots
  
api_key = ""
  
paralleldots.set_api_key(api_key)
  
my_list = []
  
for each_tweet in tweets['statuses']:
    
	analyze = paralleldots.sentiment(each_tweet['text'])
    
	my_list.append(analyze)
  
return my_list
  


def get_num_followers(query):
  
tweets = get_tweets(query)
  
import json
  
num_followers=0
  
print json.dumps(tweets)
  
for each_tweet in tweets['statuses']:
    
my_dict={}
    
my_dict['screen_name']=each_tweet['user']['screen_name']
    
my_dict['followers_count']=each_tweet['user']['followers_count']
    
print my_dict
    
#print(each_tweet['user']['screen_name'] & each_tweet['user']['followers_count'])
    
num_followers+=each_tweet['user']['followers_count']
  
return num_followers
  


def get_sentiment(query):
  
my_list = get_analyse(query)
  
import json
  
nutweet=0
  
ntweet=0
  
ptweet=0
  
#print(json.dumps(my_list))
  
for i in my_list:
    
if (i['sentiment'] == "neutral"):
      
nutweet+=1
    
elif (i['sentiment'] == "negative"):
      
ntweet+=1
    
else:
      
ptweet+=1
  
print "positive tweets are:%s"%ptweet
  
print "neutral tweets are:%s"%nutweet
  
print "negative tweets are:%s"%ntweet
    


def get_ln_tym_loc(query):
  
import pandas as pd
  
import numpy as np
  
hashtag = "#" + query
  
tweets = get_tweets(query)
  
for each_tweet in tweets['statuses']:
    
my_dict={}
    
my_dict['location']=each_tweet['user']['location']
    
my_dict['time_zone']=each_tweet['user']['time_zone']
    
my_dict['lang'] = each_tweet['user']['lang']
    
print my_dict
  
public_tweets = api.GetSearch(hashtag, count=10)
  
data = pd.DataFrame()
  
data['location']=[tweets.user.location for tweets in public_tweets]
  
data['lang']=[tweets.user.lang for tweets in public_tweets]
  
data['time_zone']=[tweets.user.time_zone for tweets in public_tweets]
  
print("\n counter for various locations:")
  
print data['location'].value_counts()
  
print("\n counter for various languages:")
  
print data['lang'].value_counts()
  
print("\n counter for various time_zones:")
  
print data['time_zone'].value_counts()
  


def get_compare():
  
import tweepy
  
import re
  
import json
  
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
  
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  
api = tweepy.API(auth)

  
#####Narendra Modi 

  
new_tweets1 = api.user_timeline(screen_name ='@narendramodi',count=200, tweet_mode="extended")
  
#tweets1 = [[tweet.full_text] for tweet in new_tweets1]
  
#print json.dumps(tweets1)
  
my_text1 = []
  
for tweet in new_tweets1:
    
text1 = tweet.full_text
    
my_text1.append(text1)
    
str1 = ''.join(my_text1)
    
result1 = re.sub(r"http\S+", "", str1)
    
#print(result1)

  
patterns1 = ['\sUSA\s','\sUS\s','\sAmerica\s','\sUnited states of America\s']
  
#str1.count('US')
  
count1=0
  
print("Check if PM Modi has mentioned 'USA','US','America' OR 'United States of America' in his last 200 tweets:")
  
for pattern in patterns1:
    
#print('looking for "%s" in "%s" ->'%(pattern,str1))
    
if re.search(pattern,result1):
      
print('"%s" : found'%(pattern))
      
count1+=1
    
print('\nno. of times %s found : %s'%(pattern,count1))  

  

#####DonaldTrump

  
new_tweets2 = api.user_timeline(screen_name ='@realDonaldTrump',count=200, tweet_mode="extended")
  
#tweets2 = [[tweet.full_text] for tweet in new_tweets2]
  
#print json.dumps(tweets2)
  
my_text2 = []
  
for tweet in new_tweets2:
    
text2 = tweet.full_text
    
my_text2.append(text2)
    
str2 = ''.join(my_text2)
    
result2 = re.sub(r"http\S+", "", str2)
    
#print(result2)

  
patterns2 = ['\sindia\s','\sIndia\s']
  
#str2.count('India')
  
count2=0
  
print("\nCheck if Donald Trump has mentioned 'india' OR 'India' in his last 200 tweets:")
  
for pattern in patterns2:
    
#print('looking for "%s" in "%s" ->'%(pattern,str2))
    
if re.search(pattern,str2):
      
print('"%s" : found'%(pattern))
      
count2+=1
    
print('\nno. of times %s found : %s'%(pattern,count2))
  


def get_top_words():
  
import nltk
  
from nltk.corpus import stopwords
  
from nltk.tokenize import word_tokenize
  
nltk.download('stopwords') 
  
nltk.download('punkt')
  
stop_words = set(stopwords.words('english'))
  
import tweepy
  
import re
  
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
  
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  
api = tweepy.API(auth)
  
new_tweets = api.user_timeline(screen_name ='@narendramodi',count=200, tweet_mode="extended")
  
print("--------------")
  m
y_text = []
  
for tweet in new_tweets:
    
text = tweet.full_text
    
my_text.append(text)
  
str1 = ''.join(my_text)
  
result = re.sub(r'[^\w]', ' ', str1)
  
result1 = re.sub(r"http\S+", "", result)
  
  
word_tokens = word_tokenize(result1)

  
filtered_sentence = [w for w in word_tokens if not w in stop_words]
  
filtered_sentence = []
  
for w in word_tokens:
    
if w not in stop_words:
      
filtered_sentence.append(w)
  
str2 = ''.join(filtered_sentence)

  
import pandas as pd
  
df = pd.DataFrame({'col':filtered_sentence})
  
print("\nTop 10 words used by PM Modi are as follows:")
  
top = df.col.str.split(expand=True).stack().value_counts()[1:11,]
  
print(top)
  


def get_status_update(query):
  
import tweepy
  
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
  
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  
api = tweepy.API(auth)
  
api.update_status(query)
    


def main():
  
while(True):
    
user_choice = input("1. Tweet Retreival and their status class.\n"
                        
		    "2. Count the total no. of followers of people Tweeting using a certain Hashtag.\n"
                        
		    "3. Determine the location, Timezone and Language of people Tweeting using a certain Hashtag.\n"
                        
		    "4. Numbers of times Modi has referred to US in the past 200 Tweets compared to how many times Trump has mentioned India.\n"
                        
		    "5. Determine the Sentiment of people Tweeting using a certain Hashtag.\n"
                        
		    "6. Top 10 words used by PM Modi on Twitter.\n"
                        
		    "7. Tweet a message from your account.\n"
                        
		    "8. Exit.\n")
    
if user_choice==1:
      
user_input = raw_input("Enter the Hashtag:")
      
get_status(user_input)
    
elif user_choice==2:
      
user_input = raw_input("Enter the Hashtag:")
      
print "\n\n Max. no. of people who might have seen this Hashatg: %s" %(get_num_followers(user_input))
    
elif user_choice==3:
      
user_input = raw_input("Enter the Hashtag:")
      
get_ln_tym_loc(user_input)
    
elif user_choice==4:
      
get_compare()
    
elif user_choice==5:
      
user_input = raw_input("Enter the Hashtag:")
      
get_sentiment(user_input)
    
elif user_choice==6:
      
get_top_words()
    
elif user_choice==7:
      
user_input = raw_input("Enter the Status:")
      
get_status_update(user_input) 
    
elif user_choice==8:
        
break
    
else:print("i didn't get that, plz try again.\n")
          


main()

