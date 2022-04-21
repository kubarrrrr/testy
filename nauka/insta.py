import os 
import glob
cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])
from instaBot import Bot

bot = Bot()
bot.login(username='analogowe.love', password='haslomaslo2')
