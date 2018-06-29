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
    # 'http://visit.kaunas.lt/en/to-do/health-and-leisure/spa-and-wellness-centers/sauleja-spa/',
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
    # 'http://visit.kaunas.lt/en/medical-tourism/medical-tourism-facilitator/wellness-travels/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/dental-clinic-eraimplant/',
    'http://visit.kaunas.lt/en/medical-tourism/orthopaedy/ab-ortopedijos-technika-orthopaedy/',
    'http://visit.kaunas.lt/en/medical-tourism/spa-and-rehabilitation/medical-spa-versme/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/dental-clinic-neodenta/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/dental-clinic-arinija/',
    'http://visit.kaunas.lt/en/medical-tourism/plastic-surgery/era-esthetic/',
    'http://visit.kaunas.lt/en/medical-tourism/general-practice-and-diagnostics/the-general-medicine-practice-clinic/',
    'http://visit.kaunas.lt/en/medical-tourism/aesthetic-medicine/era-esthetic-lazerines-dermatologijos-klinika/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/dental-clinic-sidanta/',
    # 'http://visit.kaunas.lt/en/medical-tourism/medical-tourism-facilitator/medvisus/',
    # 'http://visit.kaunas.lt/en/to-do/health-and-leisure/spa-and-wellness-centers/east-island-spa/',
    'http://visit.kaunas.lt/en/medical-tourism/aesthetic-medicine/sana-beauty/',
    'http://visit.kaunas.lt/en/medical-tourism/plastic-surgery/gp-clinic/',
    'http://visit.kaunas.lt/en/medical-tourism/aesthetic-medicine/grozio-akademija/',
    'http://visit.kaunas.lt/en/medical-tourism/dentistry/international-dental-clinic-pro-implant/'
]

# Open chrome
#driver.get('http://visit.kaunas.lt/en/medical-tourism/dentistry/')
# driver.get('http://visit.kaunas.lt/en/medical-tourism/dentistry/?start=10')


# # extend the page with the 'more' button by running JS code
# driver.execute_script("document.getElementsByClassName('button-white')[0].click()")
#
# # find all links to the places
# links = []
# titles = driver.find_elements_by_class_name('product-title')
# for title in titles:
#     link = title.get_attribute('href')
#     print(link)
#     links.append(link)

#empty list for appending new data and writing to csv
b = []

# Open a file to write csv to
outputFile = open('medicalTourism.csv', 'w', newline='', encoding='utf-8')
outputWriter = csv.writer(outputFile)

# Go through the pages and select the wanted elements
for link in a:
    driver.get(link)

    # escape the popup
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    # find the element
    title = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/h1').text
    address = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/span[1]').text
    phone_number = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/span[2]/a').text
    website = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/span[4]/a').get_attribute('href')

    # append the element to the empty list
    b.append(title)
    b.append(address)
    b.append(phone_number)
    b.append(website)

    try:
        email = driver.find_element_by_xpath('//*[@id="body"]/div[2]/div[1]/div[3]/div/span[3]/a').text
        b.append(email)
    except NoSuchElementException:
        b.append('')

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
