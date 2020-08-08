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
username_login.send_keys("throwawaytest2864")

password_login = driver.find_element_by_id("loginPassword")
password_login.send_keys("1234567a")


button = driver.find_element_by_css_selector(".m-full-width")
button.click()

time.sleep(5)

urls = ['https://www.reddit.com/r/testingground4bots/comments/i5w5ey/testing_1_2_3_4_5_6/',
	"https://www.reddit.com/r/aww/comments/i5tt92/they_were_definitely_planning_something_down_there/",
	"https://www.reddit.com/r/PrequelMemes/comments/i5m5ok/a_grevious_mistake/"]
for url in urls:
	driver.get(url)
	upvote_percent = driver.find_element_by_css_selector(".t4Hq30BDzTeJ85vREX7_M")
	print(upvote_percent.text)
	net_upvotes = driver.find_element_by_css_selector("._1E9mcoVn4MYnuBQSVDt1gC")
	print(net_upvotes.text)








