import requests
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from time import sleep
import POM_test_JakubRuszkowski_polska_jazda as pom


def test_category():
    r = requests.get(pom.strona)
    assert r.status_code == 200 , 'error 403, probably something is broken'

    
browser = webdriver.Firefox()
browser.get(pom.url2)
sleep(2)
opiniemoto = browser.find_element(By.XPATH, pom.odnosnik).click()
sleep(2)
browser.close()



