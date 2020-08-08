from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "/Users/Wish/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.twitter.com/login")

username_login = driver.find_element_by_name("session[username_or_email]")
username_login.send_keys("throwaway394959")

password_login = driver.find_element_by_name("session[password]")
password_login.send_keys("1234567a")

button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div")
button.click()

time.sleep(5)

#driver.get("https://www.reddit.com/r/test/submit")

"""
search_bar = driver.find_element_by_id("header-search-bar")
search_bar.send_keys("r/test")
search_bar.send_keys(Keys.ENTER)
"""
'''
=======
link = driver.find_element_by_link_text("Login")
link.click()
>>>>>>> 87296406ae9df73e28ccbf261078f66875a58f47
'''