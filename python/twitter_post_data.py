from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_twitter_analytics(url):
    PATH = "/Users/briantaylor/Desktop/important/chromedriver"
    driver = webdriver.Chrome(PATH)

    driver.get(url)
    time.sleep(2)

    likes = driver.find_element_by_css_selector('.css-1dbjc4n')
    data = likes.text[:1000].split('\n')
    facts = {'retweets': "0", 'comments': "0", 'likes': "0", 'retweets_comments': "0"}
    """So all of these if/else, try/except blocks are there to help scrape data from
    many of the different possible configurations of a tweet. As not every configuration
    provides the data necessary, a 0 is returned for any figure not gotten.
    """
    for i in range(len(data)):
        if data[i].strip() == "Retweets and comments":
            facts['retweets_comments'] = data[i-1]
        elif data[i].strip() == "Retweets" or data[i].strip() == "Retweet":
            facts['retweets'] = data[i-1]
        if data[i].strip() == "Likes" or data[i].strip() == "Like":
            facts['likes'] = data[i-1]
        elif data[i].strip() == "More Tweets":
            try: 
                int(data[i-1][0])
                facts['likes'] = data[i-1]
            except:
                continue
        elif data[i].strip() == "Replies":
            try:
                int(data[i-3][0])
                facts['retweets'] = data[i-3]
                facts['comments'] = data[i-2]
                facts['likes'] = data[i-1]
            except:
                facts['retweets'] = data[i-8]
                facts['comments'] = data[i-7]
                facts['likes'] = data[i-6]

    for fact in facts:
        if "K" in facts[fact]:
            facts[fact] = facts[fact].replace("K", "000")
            if "." in facts[fact]:
                facts[fact] = facts[fact][:-1].replace(".","")
        try:
            facts[fact] = int(facts[fact])
        except:
            facts[fact] = 0
    retweets_comments = facts['retweets'] + facts['comments'] + facts['retweets_comments']

    final = {'likes': facts['likes'], 'retweets_comments': retweets_comments}
    
    return(final)

if __name__ == '__main__':
    urls = []
    urls.append('https://twitter.com/elonmusk/status/1290056061253165057?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet')
    urls.append('https://twitter.com/olivegarden/status/970347418146484224')
    urls.append('https://twitter.com/BarackObama/status/1291440263404167177')
    urls.append('https://twitter.com/JoeBiden/status/1292264334287044609')
    urls.append('https://twitter.com/throwaway394959/status/1292315600849473537')
    urls.append('https://twitter.com/throwaway394959/status/1292065983146758145')
    urls.append('https://twitter.com/sroodsari/status/1283715339818119168?s=12')
    urls.append('https://twitter.com/EbThen/status/1292139344048918529')
    urls.append('https://twitter.com/spaghettybaby/status/1285325123851915265?s=12')

    for url in urls:
        print(get_twitter_analytics(url))

