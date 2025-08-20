from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications": 2}  # 2 = Block   # notification  of
chrome_options.add_experimental_option("prefs", prefs)

s = Service(r"C:\Users\acer\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get("https://learnwith.campusx.in/")
time.sleep(50)

driver.get("https://learnwith.campusx.in/courses/Data-Science-Master-Program-63a30827e4b0c0f22f756324")
time.sleep(5)

link = driver.find_element(By.XPATH, '/html/body/div[1]/header/section[2]/a[1]')
link.click()

time.sleep(10)
driver.quit()   #  this is the automated  code only  you can use  for automation



