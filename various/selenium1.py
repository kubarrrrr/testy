from selenium import webdriver


from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class Insta_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://instagram.com")

    def test_sauce_login(self):
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('fotograf.koszalin')  #login
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('haslomaslo2')  #password
        sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click() #login click

        sleep(5)
        self.driver.get('https://www.instagram.com/fotograf.koszalin/following/')
        sleep(5)
        while True:
            follow = self.driver.find_element(By.TAG_NAME, '//*[contains(text(), "Following")]').click()
                
        sleep(5)

if __name__ == "__main__":
    unittest.main()