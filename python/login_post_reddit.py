from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login_and_post_reddit(username, password, header, message, sub):

	PATH = "/Users/abina/Desktop/chromedriver"
	driver = webdriver.Chrome(PATH)

	driver.get("https://www.reddit.com/login/")

	username_login = driver.find_element_by_id('loginUsername')
	username_login.send_keys(username)

	password_login = driver.find_element_by_id("loginPassword")
	password_login.send_keys(password)

	button = driver.find_element_by_css_selector(".m-full-width")
	button.click()

	time.sleep(10)

	urls = []

	driver.get(f"https://www.reddit.com/{sub}/submit")

	title = driver.find_element_by_css_selector(".PqYQ3WC15KaceZuKcFI02")
	title.send_keys(header)

	body = driver.find_element_by_css_selector(".notranslate")
	body.send_keys(message)


	post_btn = driver.find_element_by_css_selector("._2JBsHFobuapzGwpHQjrDlD")
	post_btn.click()

	time.sleep(2)
	urls.append(driver.current_url)

	return urls
	#The list of urls will enable us to easily track posts to gain statistics about those posts later.
if __name__ == '__main__':
	username = "throwaway3949596"
	password = "1234567a"
	header = "This is just a sample post, nothing to see here"
	message = "Trying to automate posting to reddit, this was posted"
	message += "by a bot, feel free to ignore, no big deal either way"
	sub = "r/BotsPlayHere"
	login_and_post_reddit(username, password, header, message, sub)

#Alright, so, it works if it is allowed to post multiple times. However, if it is thrown an error,
#such as being unable to post, it will not continue beyond that error. I am, 
#at this point, unable to resolve the issue. I'm also not entirely sure why selenium/chromedriver
#rely so heavily on being able to post.


#<button class="_2JBsHFobuapzGwpHQjrDlD _18Bo5Wuo3tMV-RDB8-kh8Z ">Post</button>

#_2JBsHFobuapzGwpHQjrDlD
"""
search_bar = driver.find_element_by_id("header-search-bar")
search_bar.send_keys("r/test")
search_bar.send_keys(Keys.ENTER)
"""
'''

link = driver.find_element_by_link_text("Login")
link.click()
'''