from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

import csv
import time

#fix the starting time of running the script
start_time = time.clock()

# Open a new csv file to save(write) the results to
outputFile = open('eat-drink.csv', 'w', newline='', encoding='utf-8')
outputWriter = csv.writer(outputFile)

# Create a list with column titles and write it to the csv as the first line
column_names = ['ID', 'Source', 'Title', 'Address', 'Phone', 'Email', 'Website', 'Working Hours', 'Description', 'Category']
outputWriter.writerow(column_names)

# empty list for adding a new line of data to write to csv
empty_list = []

# xpaths for the wanted elements
title_xpath ='//*[@id="body"]/div[2]/div[1]/div[3]/div/h1'
address_xpath = '//*[@id="body"]/div[2]/div[1]/div[3]/div/span[1]'
phone_xpath = '//*[@id="body"]/div[2]/div[1]/div[3]/div/span[2]/a'
email_xpath ='//*[@id="body"]/div[2]/div[1]/div[3]/div/span[3]/a'
website_xpath = '//*[@id="body"]/div[2]/div[1]/div[3]/div/span[4]/a'
working_hours_xpath = '//*[@id="body"]/div[2]/div[1]/div[3]/div/span[5]'
description_xpath = '//*[@id="body"]/div[2]/div[2]/div'

#list with all the xpaths
xpaths = [title_xpath, address_xpath, phone_xpath, email_xpath, website_xpath, working_hours_xpath, description_xpath]


# a function that keeps clicking the 'More' button until all results are displayed
def extend_page():
    while True:
        time.sleep(3)
        try:
            button = driver.find_element_by_class_name('button-white')
            button.click()
        except NoSuchElementException:
            break

# a function that finds all the elements (links to them) and their respective categories
def links_and_categories():
    titles = driver.find_elements_by_class_name('product-title')
    links = [title.get_attribute('href') for title in titles]
    categories = driver.find_elements_by_class_name('category-title')
    category_names = [category.text for category in categories]
    dictionary = dict(zip(links, category_names))
    # print(dictionary)
    return dictionary

# a variable to generate IDs
id = 1

# Create a driver, open the link in Chrome and escape the popup
driver = webdriver.Chrome()
driver.get('http://visit.kaunas.lt/en/eat-and-drink/')
ActionChains(driver).send_keys(Keys.ESCAPE).perform()

# run the function that extends the page and
# give 3 secs for the browser to load all elements
extend_page()
time.sleep(3)

# get a variable for the dictionary of links and categories
dictionary = links_and_categories()

#loop the links and categories in the dictionary
for link, category in dictionary.items():
    #add the id and the source page to the empty list
    empty_list.append(id)
    empty_list.append(link)

    # go to each link
    # find elements and append to the empty list, or enter empty values if elements not found
    driver.get(link)
    time.sleep(3)

    for object in xpaths:
        try:
            element = driver.find_element_by_xpath(object).text
            empty_list.append(element)
        except NoSuchElementException:
            empty_list.append('')

    #add the category to the list from the dictionary
    empty_list.append(category)

    # write the row with appended element values (empty_list) to the output .csv file
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