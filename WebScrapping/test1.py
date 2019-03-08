# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:25:38 2019

@author: harshvardhan
"""
import os
from selenium import webdriver

chromedriver = "/Users/adam/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://stackoverflow.com")
driver.quit()