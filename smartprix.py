from  selenium import webdriver
from selenium .webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service(r"C:\Users\acer\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://www.smartprix.com/mobiles")
time.sleep(5)

# Find  label  instead of input due  to  dynamic filtering click load buttons
checkbox_label=driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input')
checkbox_label.click()
time.sleep(5)
Checkbox_label1=driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input')
Checkbox_label1.click()
time.sleep(5)
Checkbox_label2=driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/div[1]/div[2]/div[3]')
Checkbox_label2.click()
time.sleep(2)


  
old_height=driver.execute_script("return document.body.scrollHeight")  # for require loop
while True:
  driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/div[1]/div[2]/div[3]')
  time.sleep(5)
  new_height=driver.execute_script("return document.body.scrollHeight") # find out new height because break the loop and scrab all pages
  print(old_height)
  print(new_height)

  if new_height ==old_height:
    break

  old_height=new_height

html=driver.page_source

with open('smartprix1.html','w',encoding='utf-8') as f:
    f.write(html)


