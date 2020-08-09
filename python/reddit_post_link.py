from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = r"C:\Users\srjnk\Documents\chromedriver\chromedriver.exe"
# PATH = "/Users/briantaylor/Desktop/important/chromedriver"
options = Options()
options.binary_location = binary_location=r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"
options.headless = True
driver = webdriver.Chrome(PATH, chrome_options=options)
driver.get("https://www.reddit.com/login/")


username_login = driver.find_element_by_id('loginUsername')
username_login.send_keys("throwaway3949596")

password_login = driver.find_element_by_id("loginPassword")
password_login.send_keys("1234567a")

button = driver.find_element_by_css_selector(".m-full-width")
button.click()

time.sleep(10)

driver.get(f"https://www.reddit.com/r/testingground4bots/submit")
link_btn = driver.find_element_by_css_selector("._2-0pxD6-cM6bWeb73TNNhJ") 
link_btn.click()

title = driver.find_element_by_css_selector(".PqYQ3WC15KaceZuKcFI02")
title.send_keys("Testing 1 2 3 4 5 6")

body = driver.find_element_by_css_selector("._3zY6b4QJpSz1067ahq73_K")
body.send_keys("https://pybit.es/images/logo.png")

post_btn = driver.find_element_by_css_selector("._2JBsHFobuapzGwpHQjrDlD")
post_btn.click()
