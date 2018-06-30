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
driver.get('http://visit.kaunas.lt/en/eat-and-drink/')
# escape the popup
ActionChains(driver).send_keys(Keys.ESCAPE).perform()
# extend the page with the 'more' button by running JS code

time.sleep(3)
button = driver.find_element_by_class_name('button-white')
button.click()

# while True:
#     time.sleep(3)
#     button = driver.find_element_by_class_name('button-white')
#     if button.is_displayed():
#         button.click()
#         # driver.execute_script("document.getElementsByClassName('button-white')[0].click()")
#     else:
#         break

#give 3 secs for the browser to load more elements
time.sleep(3)

# find all elements (titles)
titles = driver.find_elements_by_class_name('product-title')

# extract links from the elements (links from titles)
def write_links():
    links = [title.get_attribute('href') for title in titles]
    return links

#print how many results did we collect
print(len(write_links()))

# def print_links():
#     for title in titles:
#         link = title.get_attribute('href')
#         print(link)
# print_links()

