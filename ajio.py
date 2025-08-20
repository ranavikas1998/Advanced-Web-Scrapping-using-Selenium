from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service(r"C:\Users\acer\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.ajio.com/men-backpacks/c/830201001")
time.sleep(5)

# Get window height and scroll height
height = driver.execute_script("return window.innerHeight")
old_height = driver.execute_script("return document.body.scrollHeight")

print("Window Height:", height)
print("Total Scroll Height:", old_height)

counter=1
while True:
# Scroll till bottom
   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # last page scroll down but problem it can be stop
   time.sleep(3)

   new_height=driver.execute_script("return document.body.scrollHeight")  # for last tak scroll

   print(counter)
   counter=+1
   print(old_height)
   print(new_height)

   if new_height == old_height:   # all page  loaded the data
       break
   old_height=new_height

html=driver.page_source

####--this code is save/load the html file
with open("ajio.html","w",encoding="utf-8") as f:
    f.write(html)

print(height)


