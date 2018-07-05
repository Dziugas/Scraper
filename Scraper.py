from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException

import csv
import time

#fix the starting time of running the script
start_time = time.clock()

# Create a driver and open a link in Chrome
driver = webdriver.Chrome()
driver.get('http://visit.kaunas.lt/en/eat-and-drink/')

# escape the popup
ActionChains(driver).send_keys(Keys.ESCAPE).perform()

# a function that keeps clicking the 'More' button until all results are displayed
def extend_page():
    while True:
        time.sleep(3)
        try:
            button = driver.find_element_by_class_name('button-white')
            button.click()
        except NoSuchElementException:
            break

# a function that finds all the elements (titles) and extract links from them
def links():
    titles = driver.find_elements_by_class_name('product-title')
    links = [title.get_attribute('href') for title in titles]
    return links

#run the function that extends the page
extend_page()

#give 3 secs for the browser to load all elements
time.sleep(3)

#run the function that collects the links and assign the result to the list variable 'titles'
title_links = links()

#print how many results we got
print(len(links()))

# Open a new csv file to save(write) the results
outputFile = open('medicalTourism.csv', 'w', newline='', encoding='utf-8')
outputWriter = csv.writer(outputFile)

# Create a list with column titles and write it to csv as the first line
column_names = ['ID', 'Source', 'Title', 'Address', 'Phone', 'Email', 'Website', 'Working Hours']
outputWriter.writerow(column_names)

# empty list for adding new line of data to write to csv
empty_list = []

# xpaths for the wanted elements
title_xpath ='//*[@id="body"]/div[2]/div[1]/div[3]/div/h1'
address_xpath = '//*[@id="body"]/div[2]/div[1]/div[3]/div/span[1]'
phone_xpath = '//*[@id="body"]/div[2]/div[1]/div[3]/div/span[2]/a'
email_xpath ='//*[@id="body"]/div[2]/div[1]/div[3]/div/span[3]/a'
website_xpath = '//*[@id="body"]/div[2]/div[1]/div[3]/div/span[4]/a'
working_hours_xpath = '//*[@id="body"]/div[2]/div[1]/div[3]/div/span[5]'

#list with all the xpaths
xpaths = [title_xpath, address_xpath, phone_xpath, email_xpath, website_xpath, working_hours_xpath]

# variable to generate IDs
id = 1

# Go through the pages and select the wanted elements
for link in title_links:
    #add the source page to the table
    empty_list.append(id)
    empty_list.append(link)

    #open link in the browser
    driver.get(link)

    # escape the popup
    # ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    # find elements and append to the empty list b, or enter empty values if elements not found
    for object in xpaths:
        try:
            element = driver.find_element_by_xpath(object).text
            empty_list.append(element)
        except NoSuchElementException:
            empty_list.append('')

    # write the element to the output .csv file
    outputWriter.writerow(empty_list)

    # empty the list for the next line of data from the next page
    empty_list = []

    # increase the id by one
    id+=1

# close the .csv file
outputFile.close()

# close driver/browser
driver.close()

#fix the end time of running the script
end_time = time.clock()

#print the time it took to run the code
print(end_time-start_time)