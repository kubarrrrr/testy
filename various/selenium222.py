from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

s = Service('C:/chromedriver.exe')
browser = webdriver.Chrome(service=s)
# url='https://duckduckgo.com'
# browser.get(url)
# sleep(2)
# search = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div[2]/form/input[1]")
# search.send_keys("test", Keys.ENTER)

url='https://duckduckgo.com'
browser.get(url)

browser.maximize_window()
searchh = browser.find_element(By.ID, 'app')
searchh.click()
