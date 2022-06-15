import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome()
driver.get('http://www.instagram.com')
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]').click()
driver.find_element(By.NAME, 'username').send_keys('fotograf.koszalin')
driver.find_element(By.NAME, 'password').send_keys('haslomaslo2')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(5)







# target the login button and click it
button = WebDriverWait(
	driver, 2).until(EC.element_to_be_clickable(
		(By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(5)

driver.get("https://www.instagram.com/fotograf.koszalin/following/")

driver.find_element_by_partial_link_text("follower").click()

pop_up_window = WebDriverWait(
	driver, 2).until(EC.element_to_be_clickable(
		(By.XPATH, "//div[@class='isgrP']")))

# Scroll till Followers list is there
while True:
	driver.execute_script(
		'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
	pop_up_window)
	time.sleep(1)

driver.quit()
