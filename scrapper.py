from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("./chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape () :
    headers = ["Name","Distance","Mass","Radius"]
    sun_data = []
    
