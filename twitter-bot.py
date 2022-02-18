#!/usr/bin/env python3

#import modules
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import warnings
import time

#store start time 
start_time = time.time()

#print acii
a = '''
 +-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+
 |c|o|d|e| |b|y| |m|a|n|s|o|o|r|.|c|o|d|e|
 +-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+
'''
print(a)

#ignore warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

#set option for headless browser
options = Options()
options.headless = True

#ask msg
msg = input("Enter your message: \n")

#creds
uname = "mansoorbarri"
pwd = "Yamahateslar1x1@twitter"

#open firefox
driver = webdriver.Firefox(options=options)

#go to login page
driver.get("https://twitter.com/i/flow/login")
time.sleep(5)

#click on username field
username = driver.find_element_by_name("text")
username.click()

#print progress
print("Logging in twitter")

#type the username
username.send_keys(uname)

#click "next"
driver.find_element_by_css_selector("div.css-18t94o4:nth-child(6) > div:nth-child(1)").click()
time.sleep(1)

#click on the password field
password = driver.find_element_by_name("password")
password.click()

#type the password
password.send_keys(pwd)

#click login
driver.find_element_by_css_selector(".r-ywje51 > div:nth-child(1)").click()

#wait for the page to loaod
time.sleep(5)

#print progress
print("Tweeting")
#click on "what's happenning?"
driver.find_element_by_css_selector(".public-DraftStyleDefault-block").click()

#type your msg
text = driver.find_element_by_css_selector(".notranslate")
text.send_keys("", msg, " ")

#tweet!
driver.find_element_by_css_selector("div.r-l5o3uw:nth-child(4)").click()

#print progress
print("Tweeted")

#close the browser
driver.close()

#print time it took
print("time to complete the tweet", time.time() - start_time)
