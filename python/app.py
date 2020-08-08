from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/Users/briantaylor/Desktop/important/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.reddit.com/login/")

username_login = driver.find_element_by_id('loginUsername')
username_login.send_keys("throwaway3949596")

password_login = driver.find_element_by_id("loginPassword")
password_login.send_keys("1234567a")

button = driver.find_element_by_css_selector(".m-full-width")
button.click()

time.sleep(5)

driver.get("https://www.reddit.com/r/test/submit")

"""
search_bar = driver.find_element_by_id("header-search-bar")
search_bar.send_keys("r/test")
search_bar.send_keys(Keys.ENTER)
"""
