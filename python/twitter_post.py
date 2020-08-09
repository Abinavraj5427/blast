from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from twitter_api import post_twitter
import time


def login_and_post_twitter(username, password, message):
	# PATH = "/Users/briantaylor/Desktop/important/chromedriver"
	PATH = "/Users/Wish/Downloads/chromedriver"

	# options = Options()
	# options.headless = True
	# driver = webdriver.Chrome(PATH, chrome_options=options)
	driver = webdriver.Chrome(PATH)

	driver.get("https://www.twitter.com/login")
	time.sleep(1)
	username_login = driver.find_element_by_name("session[username_or_email]")
	username_login.send_keys(username)

	password_login = driver.find_element_by_name("session[password]")
	password_login.send_keys(password)

	button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div")
	button.click()


	body = driver.find_element_by_css_selector(".public-DraftStyleDefault-block")
	body.send_keys(message)
	button1 = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]")
	button1.click()
	#body.send_keys(Keys.COMMAND, Keys.ENTER)
	#time.sleep(4)
	#driver.get(f"https://www.twitter.com/{username}")
	#time.sleep(2)
	#post = driver.find_element_by_class_name("css-1dbjc4n")
	#post.click()
	#time.sleep(5)
	#return post_twitter(username)



#if __name__ == '__main__':
#	login_and_post_twitter("throwaway3949596@gmail.com", "1234567a","Test message #29")



