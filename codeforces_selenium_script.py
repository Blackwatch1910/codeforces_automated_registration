# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

"""
To enable firebug extention
fp = webdriver.FirefoxProfile()
fp.add_extension(extension='firebug-2.0.8.xpi')
fp.set_preference("extensions.firebug.currentVersion", "2.0.8") #Avoid startup screen
driver = webdriver.Firefox(firefox_profile=fp)
"""

driver = webdriver.Firefox()
driver.get("http://www.codeforces.com/contests")
assert "Codeforces" in driver.title
elem = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.CSS_SELECTOR, "div.lang-chooser"))
)

def login():
    print "Enter Handle :",
    handle=raw_input()
    print "Enter passsword :",
    password=raw_input()
    elem=driver.find_element_by_link_text('Enter').click()
    handle_elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "handle"))
    )
    handle_elem.send_keys(handle)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_class_name('submit').submit()
    elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.lang-chooser"))
    )
    if handle in elem.text:
        return
    else:
        print "Invalid handle or password!"
        login()

if 'Enter' in elem.text :
    login()

try:
    while True:
        elem=driver.find_element_by_class_name("datatable")
        elem.find_element_by_partial_link_text('Register').click()
        elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.submit"))
        )
        elem.submit()
        elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.lang-chooser"))
        )
except NoSuchElementException :
    print 'Error occured. please enable firebug and debug.'
    pass
finally:
    print 'All Done.'

#driver.close()
