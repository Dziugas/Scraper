from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException

import csv
import time

import bs4
import requests

# Open a new csv file to save(write) the results to
outputFile = open('to-see.csv', 'w', newline='', encoding='utf-8')
outputWriter = csv.writer(outputFile)

# Create a list with column titles and write it to the csv as the first line
column_names = ['ID', 'Source', 'Title', 'Address', 'Phone', 'Email', 'Website', 'Working Hours', 'Date', 'Price', 'Category']
outputWriter.writerow(column_names)

# empty list for adding a new line of data to write to csv
empty_list = []

# css selectors for the wanted elements
title_selector = '.info-container h1'
address_selector = '.ticekt-place'
phone_selector = '.ticekt-phone'
email_selector = '.ticekt-mail'
website_selector = '.ticekt-link'
working_hours_selector = '.ticekt-calendar'
date_selector = '.ticekt-calendar'
price_selector = '.ticekt-price'
# description_selector = '.product-wrapper div p span' - selector does not work


#list with all the css selectors
css_selectors = [title_selector, address_selector, phone_selector, email_selector, website_selector, working_hours_selector, date_selector, price_selector]


# a function that keeps clicking the 'More' button until all results are displayed
def extend_page():
    while True:
        time.sleep(4)
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

# Create a driver, open the link in Chrome - automatically set to scrape the English content
driver = webdriver.Chrome()
driver.get('http://visit.kaunas.lt/en/to-see/')

#to scrape in German
# driver.get('http://visit.kaunas.lt/de/sehen/')
#to scrape in Lithuanian
# driver.get('http://visit.kaunas.lt/lt/ka-pamatyti/')
#to scrape in Russian
# driver.get('http://visit.kaunas.lt/ru/page-9/')

#Escape the popup
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

    # for each link get the dom using Beautiful Soup
    # select elements and append to the empty list, or enter empty values if elements are not found
    agent = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    res = requests.get(link, headers=agent)
    dom = bs4.BeautifulSoup(res.text, "html.parser")
    for object in css_selectors:
        elements_raw = dom.select(object)
        elements = [element.getText() for element in elements_raw]
        if len(elements)>0:
            empty_list.append(elements[0])
        else:
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

#print the time it took to run the code
print(time.perf_counter())