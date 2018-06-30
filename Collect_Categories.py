from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException

import time

# Create a driver & open the given link Chrome
driver = webdriver.Chrome()
driver.get('http://visit.kaunas.lt/en/eat-and-drink/')

# escape the popup
ActionChains(driver).send_keys(Keys.ESCAPE).perform()

#give 3 secs for the browser to load all elements
time.sleep(3)

# find all elements (titles) and extract links from them
def category_links():
    categories = driver.find_elements_by_css_selector('#body > div.inside-nav > div > nav > a')
    cat_links = [title.get_attribute('href') for title in categories]
    del cat_links[0]
    return cat_links

#print how many results we got
print(len(category_links()))
print(category_links())
