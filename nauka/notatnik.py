import requests
import re


page = requests.get('https://www.worldometers.info/coronavirus/country/poland')
f = open('data_nowa.txt', 'w')
pattern = r'Poland COVID: (\d,{0,1}\d{0,},{0,1}\d{0,})'
obj = re.search(pattern, page.text)
print(obj.group(1))