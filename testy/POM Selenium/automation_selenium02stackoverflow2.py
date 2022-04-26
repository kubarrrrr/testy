from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
# from selenium.webdriver.chrome.options import Options
import POM_automation_selenium02stackoverflow2 as pom


browser = webdriver.Firefox()
browser.get(pom.url)

sleep(3)

def cookies2():
    return browser.find_element(By.XPATH, pom.cookies).click()

cookies2()
search = browser.find_element(By.NAME, pom.search)
search.send_keys("tekst", Keys.ENTER)



sleep(2)
cookies2()
# captcha = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]').click()
sleep(3)
browser.close()
print("udało się!!!!")
