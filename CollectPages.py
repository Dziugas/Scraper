from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException

import csv

import time

# Create a driver
driver = webdriver.Chrome()
# Open chrome
driver.get('http://visit.kaunas.lt/en/medical-tourism/')
# escape the popup
ActionChains(driver).send_keys(Keys.ESCAPE).perform()
# extend the page with the 'more' button by running JS code

#execute JS script to find and activate the "More" button for more results
driver.execute_script("document.getElementsByClassName('button-white')[0].click()")


time.sleep(10)

# find all links to the places
titles = driver.find_elements_by_class_name('product-title')

def print_links():
    for title in titles:
        link = title.get_attribute('href')
        print(link)

print_links()

