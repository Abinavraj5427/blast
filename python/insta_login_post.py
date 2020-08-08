from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "/Users/briantaylor/Desktop/important/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.facebook.com")

username = driver.find_element_by_id("email")
username.send_keys("bptincali@gmail.com")

password = driver.find_element_by_id('pass')
password.send_keys("1234567a")
password.send_keys(Keys.ENTER)


time.sleep(10)
driver.get("https://www.facebook.com")
body 

"""
password_login = driver.find_element_by_name("password")
password_login.send_keys("1234567a")
password_login.send_keys(Keys.ENTER)
"""

time.sleep(10)

