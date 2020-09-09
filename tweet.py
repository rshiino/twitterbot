import os
import tweepy
from keys import consumer_key, consumer_secret, access_token, access_token_secret

UPDATE_URL = 'https://api.twitter.com/1.1/statuses/update.json'

def lambda_handler(event, context):

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)
	r = api.update_status(event['message'])
	return 0

if __name__ == "__main__":
	import sys
	import json
	lambda_handler(json.loads(sys.argv[1]), {})