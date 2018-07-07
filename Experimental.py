from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time


driver = webdriver.Chrome()
driver.get('http://visit.kaunas.lt/en/medical-tourism/')

# escape the popup
ActionChains(driver).send_keys(Keys.ESCAPE).perform()

time.sleep(3)

# def categories():
#     categories = driver.find_elements_by_css_selector('#body > div.inside-nav > div > nav > a')
#     del categories[0:2]
#     category_link = []
#     category_text = []
#     for category in categories:
#         category_link.append(category.get_attribute('href'))
#         category_text.append(category.text)
#     dictionary = dict(zip(category_text, category_link))
#     print(dictionary, )
#     return dictionary
#
# categories()


def links_and_categoryNames():
    titles = driver.find_elements_by_class_name('product-title')
    links = [title.get_attribute('href') for title in titles]
    categories = driver.find_elements_by_class_name('category-title')
    category_names = [category.text for category in categories]
    dictionary = dict(zip(links, category_names))
    print(dictionary)
    return dictionary

links_and_categoryNames()