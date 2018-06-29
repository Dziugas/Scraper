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

# manually collected page urls:
# some don't work, maybe because not all elements are available

a = [
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/dental-clinic-angitia/',
    'http://visit.kaunas.lt/en/to-do/health-and-leisure/spa-and-wellness-centers/sauleja-spa/',
    'http://visit.kaunas.lt/en/medical-tourism/plastic-surgery/clinic-beauty-world/',
    'http://visit.kaunas.lt/en/medical-tourism/spa-and-rehabilitation/royal-spa-residence/',
    'http://visit.kaunas.lt/en/to-do/health-and-leisure/spa-and-wellness-centers/5-senses/',
    'http://visit.kaunas.lt/en/medical-tourism/spa-and-rehabilitation/medical-spa-egles-sanatorija/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/dental-clinic-malo-clinic-dpc/',
    'http://visit.kaunas.lt/en/medical-tourism/plastic-surgery/saulius-viksraitis-plastic-surgery-center/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/dental-clinic-viadenta/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/dantu-estetika/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/clinic-of-cosmetic-dentistry-prodentas/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/kaunas-dental-clinic-denticija/',
    'http://visit.kaunas.lt/en/medical-tourism/general-practice-and-diagnostics/the-aesthetic-surgery-centre/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/kaunas-implantology-center-kic/',
    'http://visit.kaunas.lt/en/medical-tourism/spa-and-rehabilitation/medical-spa-tulpe/',
    'http://visit.kaunas.lt/en/medical-tourism/spa-and-rehabilitation/azuolynas-medical-spa/',
    'http://visit.kaunas.lt/en/medical-tourism/plastic-surgery/beauty-surgery/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/teeth-whitening-salon-smile-lab/',
    'http://visit.kaunas.lt/en/medical-tourism/medical-tourism-facilitator/wellness-travels/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/dental-clinic-eraimplant/',
    'http://visit.kaunas.lt/en/medical-tourism/orthopaedy/ab-ortopedijos-technika-orthopaedy/',
    'http://visit.kaunas.lt/en/medical-tourism/spa-and-rehabilitation/medical-spa-versme/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/dental-clinic-neodenta/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/dental-clinic-arinija/',
    'http://visit.kaunas.lt/en/medical-tourism/plastic-surgery/era-esthetic/',
    'http://visit.kaunas.lt/en/medical-tourism/general-practice-and-diagnostics/the-general-medicine-practice-clinic/',
    'http://visit.kaunas.lt/en/medical-tourism/aesthetic-medicine/era-esthetic-lazerines-dermatologijos-klinika/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/dental-clinic-sidanta/',
    'http://visit.kaunas.lt/en/medical-tourism/medical-tourism-facilitator/medvisus/',
    'http://visit.kaunas.lt/en/to-do/health-and-leisure/spa-and-wellness-centers/east-island-spa/',
    'http://visit.kaunas.lt/en/medical-tourism/aesthetic-medicine/sana-beauty/',
    'http://visit.kaunas.lt/en/medical-tourism/plastic-surgery/gp-clinic/',
    'http://visit.kaunas.lt/en/medical-tourism/aesthetic-medicine/grozio-akademija/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/international-dental-clinic-pro-implant/'
]

# empty list for appending new data and writing to csv
b = []

# Open a new csv file to save(write) the results
outputFile = open('medicalTourism.csv', 'w', newline='', encoding='utf-8')
outputWriter = csv.writer(outputFile)

# Go through the pages and select the wanted elements
for link in a:
    driver.get(link)

    # escape the popup
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    # find elements and append to the empty list b, or enter empty values if elements not found

    try:
        title = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/h1').text
        b.append(title)
    except NoSuchElementException:
        b.append('')

    try:
        address = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/span[1]').text
        b.append(address)
    except NoSuchElementException:
        b.append('')

    try:
        phone = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/span[2]/a').text
        b.append(phone)
    except NoSuchElementException:
        b.append('')

    try:
        email = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/span[3]/a').text
        b.append(email)
    except NoSuchElementException:
        b.append('')

    try:
        website = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/span[4]/a').text
        b.append(website)
    except NoSuchElementException:
        b.append('')

    try:
        working_hours = driver.find_element_by_class_name('ticekt-calendar').text
        b.append(working_hours)
    except NoSuchElementException:
        b.append('')

    # write the element to the .csv file
    outputWriter.writerow(b)

    # empty the list for the next page
    b = []

# close the .csv file
outputFile.close()

# close driver/browser
driver.close()
