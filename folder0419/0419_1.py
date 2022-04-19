import os, re, requests, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from folder0404 import usecsv
from pyModule import consoleClear
import urllib.request as ur
from bs4 import BeautifulSoup as bs

url = 'https://quotes.toscrape.com/'

#html = ur.urlopen(url)
#soup = bs(html.read(), 'html.parser')

soup = bs(ur.urlopen(url).read(),'html.parser')

consoleClear.clear()

quote = soup.find_all('div',{"class":"quote"})

print(quote[0].text)
print(re.findall(r'[a-zA-Z.].+',quote[0].text))

# for i in quote:
#     print(i.text)
# print(quote[0].text)