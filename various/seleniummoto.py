import selenium
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://duckduckgo.com/')

# driver = webdriver.Chrome(options=options, executable_path=r'C:\chromedriver.exe')


time.sleep(5)
op = driver.find_element(By.NAME, 'q')
op.send_keys('test')
# assert opinieomotocyklach == 'http://zalo001.polskajazda.pl/Porady/Opinie-o-motocyklach' , 'nieprawidlowy adres'