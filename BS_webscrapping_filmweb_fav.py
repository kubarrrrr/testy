import urllib3
from bs4 import BeautifulSoup
from tqdm import tqdm

# program do pobieranie z Filmwebu najlepszych filmów. Scrapping przy użyciu BeautifulSoup

url = 'https://www.filmweb.pl/ranking/film'
ourUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(ourUrl, "lxml")
print(soup.find('title').text)

i = 1
movieList = soup.findAll('div', attrs={'class': 'rankingType'})
for div_item in movieList:
    div = div_item.find('div', attrs={'class':'rankingType__card'})
    print(str(i) + '.',)
    header = div.findChildren('h2',attrs={'class':'rankingType__title'})
    print('film: ' + str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('utf-8', 'ignore')))
    i += 1