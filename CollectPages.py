from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException

import csv

# Create a driver
driver = webdriver.Chrome()
# Open chrome
driver.get('http://visit.kaunas.lt/en/medical-tourism/dentistry/')
# escape the popup
ActionChains(driver).send_keys(Keys.ESCAPE).perform()
# extend the page with the 'more' button by running JS code
driver.execute_script("document.getElementsByClassName('button-white')[0].click()")

# find all links to the places
titles = driver.find_elements_by_class_name('product-title')
for title in titles:
    link = title.get_attribute('href')
    print(link)