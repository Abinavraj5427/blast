import os
import tweepy
import pandas as pd

consumer_key = 'vTw9xljXAMZCoVbLuZfF1NLfF'
consumer_secret = 'oTXSNmic3AiCv7yhNSGMSTw7J1EXNUpRXgtzLQlLWC3bi0p2Fz'
access_token = '1292020112682135553-gHgSRJ8jk7WxTyzlQhwWZhW27qJIjp'
access_token_secret = '0Kpl2qYHBtAg6AUzuFuw6VPiptz8QE1N9jM6xLIRcMO87'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

api.update_status("Test tweet success")
