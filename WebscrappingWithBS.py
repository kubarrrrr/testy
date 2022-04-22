import urllib.request
import bs4 as bs


sauce = urllib.request.urlopen('https://weselle.pl').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
print(soup.find_all('p'))