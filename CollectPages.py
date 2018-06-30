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

# keep clicking the 'More' button until all results are displayed
while True:
    time.sleep(3)
    try:
        button = driver.find_element_by_class_name('button-white')
        button.click()
    except NoSuchElementException:
        break

#give 3 secs for the browser to load all elements
time.sleep(3)

# find all elements (titles) and extract links from them
def links():
    titles = driver.find_elements_by_class_name('product-title')
    links = [title.get_attribute('href') for title in titles]
    return links

#print how many results we got
print(len(links()))

