import os
import tweepy
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def post_twitter(user):
	consumer_key = 'vTw9xljXAMZCoVbLuZfF1NLfF'
	consumer_secret = 'oTXSNmic3AiCv7yhNSGMSTw7J1EXNUpRXgtzLQlLWC3bi0p2Fz'
	access_token = '1292020112682135553-gHgSRJ8jk7WxTyzlQhwWZhW27qJIjp'
	access_token_secret = '0Kpl2qYHBtAg6AUzuFuw6VPiptz8QE1N9jM6xLIRcMO87'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True)


	tweet = api.user_timeline(screen_name = user, count = 10, include_rts = True)[0]

	PATH = r"C:\Users\srjnk\Documents\chromedriver\chromedriver.exe"
	# PATH = "/Users/briantaylor/Desktop/important/chromedriver"
	options = Options()
	options.binary_location = binary_location=r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"
	options.headless = True
	driver = webdriver.Chrome(PATH, chrome_options=options)
	url = f"https://www.twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
	driver.get(url)
	print(url)
	return url

