from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random

def sleep_for_period_of_time():
    limit = random.randint(60,90)
    sleep(limit)

browser = webdriver.Chrome()

# login page
browser.get('http://www.instagram.com')
sleep(2)
browser.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]').click()
browser.find_element(By.NAME, 'username').send_keys('fotograf.koszalin')
browser.find_element(By.NAME, 'password').send_keys('haslomaslo2')
sleep(1)
browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
sleep(2)

browser.get('https://www.instagram.com/fotograf.koszalin/following/')

