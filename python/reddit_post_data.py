from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_analytics(username, password, url):
	PATH = "/Users/briantaylor/Desktop/important/chromedriver"
	driver = webdriver.Chrome(PATH)

	driver.get("https://www.reddit.com/login/")

	username_login = driver.find_element_by_id('loginUsername')
	username_login.send_keys("username")

	password_login = driver.find_element_by_id("loginPassword")
	password_login.send_keys("password")


	button = driver.find_element_by_css_selector(".m-full-width")
	button.click()

	time.sleep(5)

	driver.get(url)
	upvote_percent = driver.find_element_by_css_selector(".t4Hq30BDzTeJ85vREX7_M")
	net_upvotes = driver.find_element_by_css_selector("._1E9mcoVn4MYnuBQSVDt1gC")
	print(net_upvotes)

	analytics = {"upvote%": upvote_percent,
		"net upvotes": net_upvotes
	}


if __name__ == '__main__':
	get_analytics('https://www.reddit.com/r/PrequelMemes/comments/i619dd/ah_yes_the_negotiator/')




