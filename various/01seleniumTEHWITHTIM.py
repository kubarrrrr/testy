from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


s = Service('C:/chromedriver.exe')
browser = webdriver.Chrome(service=s)
url='https://www.techwithtim.net/'
browser.get(url)
sleep(2)
search = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/aside[1]/form/label/input")
search.send_keys("test", Keys.ENTER)

main = browser.find_element(By.ID, 'main')
print(main.text)

print(browser.title)
