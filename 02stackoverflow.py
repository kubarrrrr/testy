from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')  # Last I checked this was necessary.


s = Service('C:/chromedriver.exe')
browser = webdriver.Chrome(service=s)
url='https://stackoverflow.com/'
browser.get(url)

sleep(2)

def cookies2():
    return browser.find_element(By.XPATH, "/html/body/div[4]/div/button[1]").click()

# cookies = browser.find_element(By.className, "flex--item s-btn s-btn__primary js-accept-cookies js-consent-banner-hide").click()
cookies2()
search = browser.find_element(By.NAME, "q")
search.send_keys("tekst", Keys.ENTER)

# sleep(2)
cookies2()
sleep(3)
browser.close()
print("udało się!!!!")
