from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def get_analytics(url):
	# PATH = "/Users/briantaylor/Desktop/important/chromedriver"
	PATH = "/Users/abina/Desktop/chromedriver"
	options = Options()
	options.headless = True
	driver = webdriver.Chrome(PATH, chrome_options=options)

	driver.get(url)
	upvote_percent = driver.find_element_by_css_selector(".t4Hq30BDzTeJ85vREX7_M").text.strip()
	net_upvotes = driver.find_element_by_css_selector("._1E9mcoVn4MYnuBQSVDt1gC").text.strip()
	comments = driver.find_element_by_css_selector(".FHCV02u6Cp2zYL0fhQPsO").text.split(" ")
	comments = int(comments[0])

	if net_upvotes[-1] == "k":
		net_upvotes = int(float(net_upvotes[:-1]) * 1000)
	else:
		net_upvotes = int(net_upvotes)

	if upvote_percent[1] == "%":
		upvote_percent = int(upvote_percent[:1])
	elif upvote_percent[3] == "%":
		upvote_percent = int(upvote_percent[:3])
	elif upvote_percent[2] == "%":
		upvote_percent = int(upvote_percent[:2])

	total_votes = int((net_upvotes)//((2 * upvote_percent - 100)/100))

	total_up = int(total_votes * (upvote_percent/100))
	total_down = int(total_votes * ((100-upvote_percent)/100))


	analytics = {"upvote%": upvote_percent,
		"net upvotes": net_upvotes,
		"total votes": total_votes,
		"total downvotes": total_down,
		"total upvotes": total_up,
		"comments": comments
	}
	return analytics


if __name__ == '__main__':
	url = 'https://www.reddit.com/r/PrequelMemes/comments/i619dd/ah_yes_the_negotiator/'
	print(get_analytics(url))
	url = "https://www.reddit.com/r/berkeley/comments/i5txlk/did_anyone_notice_that_berkeley_got_namedropped/"
	print(get_analytics(url))




