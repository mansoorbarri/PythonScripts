#!/usr/bin/env python3

#import webdriver from selenium module
from selenium import webdriver

#import options for firefox from selenium
from selenium.webdriver.firefox.options import Options

#import time module
import time

#import warnings module
import warnings

#import subprocess
import subprocess

#for day
from datetime import date
import calendar

#to find out today's day
curr_date = date.today()
day = calendar.day_name[curr_date.weekday()]

#ignore Deprecationa Warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

#set option for headless browser
options = Options()
options.headless = True

if day == "Saturday":
    #set browser
    driver = webdriver.Firefox(options=options)
    #this opens the website link
    driver.get("https://www.youtube.com/c/ISPR/playlists")
    time.sleep(1)
    #click on 'I agree'
    driver.find_element_by_css_selector('.qqtRac > form:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(4)').click()
    time.sleep(1)
    #set element which you want to click with css selector from inspect page 
    driver.find_element_by_css_selector('ytd-grid-playlist-renderer.style-scope:nth-child(1) > yt-formatted-string:nth-child(5) > a:nth-child(1)').click()
    #set element which you want to click with css selector from inspect page 
    driver.find_element_by_css_selector('ytd-playlist-video-renderer.style-scope:nth-child(16) > div:nth-child(2) > div:nth-child(1) > ytd-thumbnail:nth-child(1) > a:nth-child(1)').click()
    #wait for the site to load
    time.sleep(4) 
    #store url in url variable
    url = (driver.current_url)
    #ends script
    driver.close()
    #cut playlist from video
    vurl = url[:43]
    #download video
    subprocess.run("cd ~/Desktop && yt-dlp --write-subs --sub-format 'srt' --format 'mp4' " + vurl, shell=True)
    exit()
else:
    pass

if day == "Sunday":
    #set browser
    driver = webdriver.Firefox(options=options)
    #this opens the website link
    driver.get("https://www.youtube.com/c/HumTvpak/playlists")
    time.sleep(1)
    #click on 'I agree'
    driver.find_element_by_css_selector('.qqtRac > form:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(4)').click()
    time.sleep(1)
    #playlist
    driver.find_element_by_css_selector('ytd-grid-playlist-renderer.style-scope:nth-child(8) > h3:nth-child(2) > a:nth-child(1)').click()
    #episode
    driver.find_element_by_css_selector('ytd-playlist-video-renderer.style-scope:nth-child(5) > div:nth-child(2) > div:nth-child(1) > ytd-thumbnail:nth-child(1) > a:nth-child(1)').click()
    #wait for the site to load
    time.sleep(4) 
    #store url in url variable
    url = (driver.current_url)
    #ends script
    driver.close()
    #cut playlist from video
    vurl = url[:43]
    #download video
    subprocess.run("cd ~/Desktop && yt-dlp --write-subs --sub-format 'srt' --format 'mp4' " + vurl, shell=True)
    exit()
else:
    pass

if day == "Monday":
    #set browser
    driver = webdriver.Firefox(options=options)
    #this opens the website link
    driver.get("https://www.youtube.com/c/HarPalGeoOfficial/playlists")
    time.sleep(1)
    #click on 'I agree'
    driver.find_element_by_css_selector('.qqtRac > form:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(4)').click()
    time.sleep(1)
    #playlist
    driver.find_element_by_css_selector('ytd-grid-playlist-renderer.style-scope:nth-child(4) > yt-formatted-string:nth-child(5) > a:nth-child(1)').click()
    #episode
    driver.find_element_by_css_selector('ytd-playlist-video-renderer.style-scope:nth-child(9) > div:nth-child(2) > div:nth-child(1) > ytd-thumbnail:nth-child(1) > a:nth-child(1)').click()
    #wait for the site to load
    time.sleep(4) 
    #store url in url variable
    url = (driver.current_url)
    #ends script
    driver.close()
    #cut playlist from video
    vurl = url[:43]
    #download video
    subprocess.run("cd ~/Desktop && yt-dlp --write-subs --sub-format 'srt' --format 'mp4' " + vurl, shell=True)
    exit()
else:
    pass

if day == "Wednesday":
    #set browser
    driver = webdriver.Firefox(options=options)
    #this opens the website link
    driver.get("https://www.youtube.com/c/HumTvpak/playlists")
    time.sleep(1)
    #click on 'I agree'
    driver.find_element_by_css_selector('.qqtRac > form:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(4)').click()
    time.sleep(3)
    #playlist
    driver.find_element_by_css_selector('ytd-grid-playlist-renderer.style-scope:nth-child(19) > yt-formatted-string:nth-child(5) > a:nth-child(1)').click()
    time.sleep(3)
    #episode
    driver.find_element_by_css_selector('ytd-playlist-video-renderer.style-scope:nth-child(1) > div:nth-child(2) > div:nth-child(1) > ytd-thumbnail:nth-child(1) > a:nth-child(1)').click()
    #wait for the site to load
    time.sleep(4) 
    #store url in url variable
    url = (driver.current_url)
    #ends script
    driver.close()
    #cut playlist from video
    vurl = url[:43]
    #download video
    subprocess.run("cd ~/Desktop && yt-dlp --write-subs --sub-format 'srt' --format 'mp4' " + vurl, shell=True)
    exit()
else:
    pass

if day == "Thursday":
    #set browser
    driver = webdriver.Firefox(options=options)
    #this opens the website link
    driver.get("https://www.youtube.com/c/HumTvpak/playlists")
    time.sleep(1)
    #click on 'I agree'
    driver.find_element_by_css_selector('.qqtRac > form:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(4)').click()
    time.sleep(1)
    #playlist
    driver.find_element_by_css_selector('ytd-grid-playlist-renderer.style-scope:nth-child(18) > yt-formatted-string:nth-child(5) > a:nth-child(1)').click()
    #episode
    driver.find_element_by_css_selector('ytd-playlist-video-renderer.style-scope:nth-child(1) > div:nth-child(2) > div:nth-child(1) > ytd-thumbnail:nth-child(1) > a:nth-child(1)').click()
    #wait for the site to load
    time.sleep(4) 
    #store url in url variable
    url = (driver.current_url)
    #ends script
    driver.close()
    #cut playlist from video
    vurl = url[:43]
    #download video
    subprocess.run("cd ~/Desktop && yt-dlp --write-subs --sub-format 'srt' --format 'mp4' " + vurl, shell=True)
    exit()
else:
    pass