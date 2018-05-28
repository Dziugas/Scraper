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

import csv

# List of pages to scrape
a = [
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/dental-clinic-malo-clinic-dpc/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/kaunas-implantology-center-kic/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/kaunas-dental-clinic-denticija/'
]

b = []

# Open a file to write csv to
outputFile = open('dentistry.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

# Scraping
# Open the browser
driver = webdriver.Chrome()

# Go through the pages and select the wanted elements
for url in a:
    driver.get(url)
    # escape the popup
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    # find the element
    title = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/h1').text
    # append the element to the empty list
    b.append(title)
    #write the element to the .csv file
    outputWriter.writerow(b)
    # empty the list for the next page
    b = []

#close the .csv file
outputFile.close()

# close driver/browser
driver.close()
