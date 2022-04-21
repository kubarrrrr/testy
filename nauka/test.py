from instapy import InstaPy

# I used firefox here

browser = r'C:\Program Files\Mozilla Firefox\firefox.exe'
want_check_browser = False

session = InstaPy(username='analogove.love',
                  password='haslomaslo2',
                  browser_executable_path=browser)
session.login()