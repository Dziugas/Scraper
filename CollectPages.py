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
driver.get('http://visit.kaunas.lt/en/medical-tourism/dentistry/')
# escape the popup
ActionChains(driver).send_keys(Keys.ESCAPE).perform()
# extend the page with the 'more' button by running JS code

#execute JS script to find and activate the "More" button for more results

time.sleep(2)

#fails on is_displayed()
button_element = driver.find_element_by_class_name('button-white')
if button_element.is_displayed():
    driver.execute_script("document.getElementsByClassName('button-white')[0].click()")
else:
    pass


time.sleep(3)

# find all links to the places
titles = driver.find_elements_by_class_name('product-title')

def write_links():
    links = []
    for title in titles:
        link = title.get_attribute('href')
        links.append(link)
    return links

print(len(write_links()))

# def print_links():
#     for title in titles:
#         link = title.get_attribute('href')
#         print(link)
# print_links()

