from  selenium import webdriver
from selenium .webdriver.chrome.service import Service
import time

s = Service(r"C:\Users\acer\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://www.smartprix.com/mobiles")
time.sleep(50)


