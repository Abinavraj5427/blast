from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time

PATH = "/Users/Wish/Downloads/chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://www.twitter.com/login")
time.sleep(1)
username_login = driver.find_element_by_name("session[username_or_email]")
username_login.send_keys("throwaway3949596@gmail.com")

password_login = driver.find_element_by_name("session[password]")
password_login.send_keys("1234567a")

button = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div")
button.click()



#time.sleep(5) 
'''
url = 'https://twitter.com/CollegeBoard/status/1291750806920798209'
driver.get(url)

likes = driver.find_element_by_css_selector(".css-1dbjc4n")
print(likes.text)
'''



urls = ['https://twitter.com/throwaway394959/status/1292065983146758145',
	"https://twitter.com/boswellhs/status/1291830495551074305",
	"https://twitter.com/CollegeBoard/status/1291750806920798209"]
for url in urls:
	driver.get(url)
	page = requests.get(url)
	soup = BeautifulSoup(page.text, "html.parser")
	
	#match the string with the css code, find the numbers after it
	retweet_comment = soup.find('span', {'class':"r-13awgt0"})
	print(retweet_comment)

	#total_number =  driver.find_element_by_css_selector(".css-16my406")
	#print(total_number.text)
