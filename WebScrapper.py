# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:51:02 2020

@author: Neha Khan
"""

# import web driver
from selenium import webdriver
import time
import csv
from bs4 import BeautifulSoup

#input username and password fields
inp_username = input("Please Enter your LinkedIn username: ")
inp_password = input("Please Enter your LinkedIn password: ")

# initialialize chromedriver
driver = webdriver.Chrome('D://chromedriver.exe')

# driver.get method() navigates to login page of LinkedIn
driver.get('https://www.linkedin.com//login')

# locate email form by_id
username = driver.find_element_by_id('username')

# send_keys() to simulate key strokes
username.send_keys(inp_username)

# locate email form by_id
password = driver.find_element_by_id('password')

# send_keys() to simulate key strokes
password.send_keys(inp_password)

# locate submit button by_xpath
log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
log_in_button.click()

#url for webscraping 
URL = 'https://www.linkedin.com/jobs/search/?keywords=ux-designer&location=Bangalore'

driver.get(URL)

# defining new variable passing two parameters
writer = csv.writer(open("D://data.csv", 'w'))

# writerow() method to the write to the file object
writer.writerow(['Job Title', 'Job Description', 'Company Name'])

time.sleep(2)

#fetch list of jobs displayed on the screen
jobs_list = driver.find_elements_by_class_name("jobs-search-results__list-item")

time.sleep(2)

row = list()

for job in jobs_list:
    #click on the job to open its description
    job.click()
    time.sleep(1)
    
    #set the cursor on the current job description
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    time.sleep(1)

    #extract the job title
    row.append(soup.find('div', {'class': 'jobs-details-top-card__content-container'}).\
               find("h2").text.strip().encode('ascii', 'ignore').decode())
    time.sleep(0.5)    
    
    #extract the job description
    row.append(soup.find(id = "job-details").text.\
               strip().encode('ascii', 'ignore').decode())
    time.sleep(0.5) 
    
    #extract the company name
    row.append(soup.find('div', {'class': 'jobs-details-top-card__company-info'}).\
               find("a").text.strip().encode('ascii', 'ignore').decode())
    time.sleep(0.5) 
    
    #insert the row into the csv
    writer.writerow(row)
    time.sleep(0.5) 
    
    row.clear()
    time.sleep(1) 
    