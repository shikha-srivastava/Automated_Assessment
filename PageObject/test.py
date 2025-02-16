import os
import os.path
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_binary = "D:/Shikha_Srivastava/chrome-win64/chrome.exe"

options = webdriver.ChromeOptions()
options.binary_location = chrome_binary
options.add_argument("start-maximized")

driver = webdriver.Chrome(
    service=Service("D:/Shikha_Srivastava/chromedriver-win64/chromedriver.exe"),
    options=options
)
driver.get("https://indeedemo-fyc.watch.indee.tv/")
