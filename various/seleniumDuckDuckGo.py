from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

s = Service('C:/chromedriver.exe')
browser = webdriver.Chrome(service=s)
url='https://www.duckduckgo.com/'
browser.get(url)
sleep(2)
search = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div/div[3]/div[2]/a").click()
# search.send_keys("test", Keys.ENTER)


print(browser.title)
browser.quit()