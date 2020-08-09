from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()

prefs = {"profile.default_content_setting_values.notifications":2}
options.add_experimental_option("prefs", prefs)


# PATH = "/Users/briantaylor/Desktop/important/geckodriver"
PATH = "/Users/abina/Desktop/chromedriver"
driver = webdriver.Chrome(PATH, chrome_options = options)

driver.get("https://www.facebook.com")

username = driver.find_element_by_id("email")
username.send_keys("throwaway3949596@gmail.com")

password = driver.find_element_by_id('pass')
password.send_keys("goosebumps10")
password.send_keys(Keys.ENTER)

post_box = driver.find_element_by_tag_name('textarea')
post_box.send_keys("HELLO WORLD")


