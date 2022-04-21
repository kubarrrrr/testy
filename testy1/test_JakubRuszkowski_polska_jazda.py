import requests
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

def test_category():
    r = requests.get('http://zalo001.polskajazda.pl/Porady/Opinie-o-motocyklach')
    assert r.status_code == 200 , 'error 403, probably something is broken'

    

s = Service('C:/chromedriver.exe')
browser = webdriver.Chrome(service=s)
# url='https://duckduckgo.com'
# browser.get(url)
# sleep(2)
# search = browser.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div[2]/form/input[1]")
# search.send_keys("test", Keys.ENTER)

url2='http://www.polskajazda.pl/Porady/Opinie-o-motocyklach/Derbi/Senda-DRD-SM'
browser.get(url2)
# sleep(2)
# opiniemoto = browser.find_element(By.LINK_TEXT, "http://zalo001.polskajazda.pl/Porady/Opinie-o-motocyklach").click()
opiniemoto = browser.find_element(By.XPATH, "(//a[contains(text(),'Opinie o motocyklach')])[2]")
opiniemoto()




