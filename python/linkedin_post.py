from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


def post_linkedin(linkedin_username, linkedin_password, message):
    options = webdriver.ChromeOptions()

    prefs = {"profile.default_content_setting_values.notifications":2}
    options.add_experimental_option("prefs", prefs)


    # PATH = "/Users/briantaylor/Desktop/important/geckodriver"
    PATH = "/Users/abina/Desktop/chromedriver"
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(PATH, chrome_options=options)
	

    driver.get("https://www.linkedin.com/")

    username = driver.find_element_by_id("session_key")
    username.send_keys(linkedin_username)

    password = driver.find_element_by_id('session_password')
    password.send_keys(linkedin_password)
    password.send_keys(Keys.ENTER)

    btn_xpath =  "//button[@class='artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary share-box-feed-entry__trigger--v2']"

    # time.sleep(3)
    post_btn = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, btn_xpath)))
    post_btn.click()

    editor_xpath =  "//div[@class='ql-editor ql-blank']"

    # time.sleep(3)
    editor = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, editor_xpath)))
    editor.send_keys(message)

    time.sleep(2)
    # driver.execute_script("document.getElementById('ember429').click();")
    postxpath = "//button[@class='share-actions__primary-action artdeco-button artdeco-button--2 artdeco-button--primary ember-view']"
    post = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, postxpath)))
    post.click()

    return driver.current_url
