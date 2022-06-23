from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import random
import time



def sleep_for_period_of_time():
    limit = random.randint(60,90)
    time.sleep(limit)

def main():

    browser = webdriver.Firefox()
    browser.get('http://www.instagram.com')
    time.sleep(1)
    browser.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]').click()
    browser.find_element(By.NAME, 'username').send_keys('fotograf.koszalin')
    browser.find_element(By.NAME, 'password').send_keys('haslomaslo2')
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
    time.sleep(5)

    browser.get('https://www.instagram.com/fotograf.koszalin/following/')
    
    time.sleep(1)
   
    
    time.sleep(6)
   


   
    while(True):
        # unfollowing loop. needs random time implementation
        try:
            #finally scrolling the popup with followed people works!
            follow_list = browser.find_element(By.CLASS_NAME, "_aano")
            browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follow_list)
            list_of_people_who_we_are_following = browser.find_elements(By.XPATH, '//div[@class="_aaes"]//*//*')
            for person in list_of_people_who_we_are_following:
                if person.text == 'Following':
                    person.click()
                    time.sleep(3)
                    try:
                        browser.find_element(By.XPATH, '//*[text()="Unfollow"]').click()
                        print('Unfollowed')
                    except Exception as e:
                        print('could not unfollow')
                    # sleep_for_period_of_time()
            
            # sleep_for_period_of_time()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()