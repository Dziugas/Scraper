# atsidaryti nauja csv faila
# atsidaryti browseri
# prasukti per visus to tipo peidzus:
# rinkti elementus ir savinti i faila
# savinti i csv faila
# Uzsavinti csv faila


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException

import csv

# Create a driver
# Open the browser
driver = webdriver.Chrome()

#manually collected page urls:
# a = [
#     'http://visit.kaunas.lt/en/medical-tourism/dentistry/dental-clinic-malo-clinic-dpc/',
#     'http://visit.kaunas.lt/en/medical-tourism/dentistry/kaunas-implantology-center-kic/',
#     'http://visit.kaunas.lt/en/medical-tourism/dentistry/kaunas-dental-clinic-denticija/',
#     'http://visit.kaunas.lt/en/medical-tourism/dentistry/dental-clinic-arinija/',
#     'http://visit.kaunas.lt/en/medical-tourism/dentistry/teeth-whitening-salon-smile-lab/'
#
# ]

# Collect a list of pages to scrape
driver.get('http://visit.kaunas.lt/en/medical-tourism/dentistry/')
# escape the popup
ActionChains(driver).send_keys(Keys.ESCAPE).perform()
# extend the page with the 'more' button by running JS code
driver.execute_script("document.getElementsByClassName('button-white')[0].click()")

# more = driver.find_element_by_css_selector('#body > div.product-list.ajax-list.category-wrapper > div.products > span:nth-child(12) > a')
# more.click()

# find all links to the places
links = driver.find_elements_by_class_name('product-title')
for element in links:
    link = element.get_attribute('href')
    links.append(link)
print(links)


#empty list for appending new data and writing to csv
b = []

# Open a file to write csv to
outputFile = open('dentistry.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

# Go through the pages and select the wanted elements
for url in a:
    driver.get(url)
    # escape the popup
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    # find the element
    title = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/h1').text
    address = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/span[1]').text
    phone_number = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/span[2]/a').text
    email = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/span[3]/a').text
    website = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/span[4]/a').get_attribute('href')
    # append the element to the empty list
    b.append(title)
    b.append(address)
    b.append(phone_number)
    b.append(email)
    b.append(website)
    #not all working hours are available
    try:
        working_hours = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/span[5]').text
        b.append(working_hours)
    except NoSuchElementException:
        b.append('')

    #write the element to the .csv file
    outputWriter.writerow(b)
    # empty the list for the next page
    b = []

#close the .csv file
outputFile.close()

# close driver/browser
driver.close()
