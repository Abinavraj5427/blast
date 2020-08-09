from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "/Users/briantaylor/Desktop/important/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.twitter.com/login")
time.sleep(1)
username_login = driver.find_element_by_name("session[username_or_email]")
username_login.send_keys("throwaway3949596@gmail.com")

password_login = driver.find_element_by_name("session[password]")
password_login.send_keys("1234567a")

button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div")
button.click()


url = 'https://twitter.com/CollegeBoard/status/1291750806920798209'
driver.get(url)

time.sleep(2)

likes = driver.find_element_by_css_selector("css-1dbjc4n")
print(likes.text)

