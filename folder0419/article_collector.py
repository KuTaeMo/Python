import os, re, requests, sys, datetime
import urllib.request as ur
from bs4 import BeautifulSoup as bs

news = 'https://news.daum.net/'

soup = bs(ur.urlopen(news).read(),'html.parser')

newsCont = soup.find_all('a',{"class":"link_txt"})

newsTitle = []

newsLink = []

for i in newsCont:
    newsTitle.append(i.text)
    newsLink.append(i.get('href'))

titleFileNm = str(datetime.date.today())+"newsTitle.txt"
linkFileNm = str(datetime.date.today())+"newsLink.txt"

with open(titleFileNm,'w') as f1:
    for i in newsTitle:
        f1.write(i)

with open(linkFileNm,'w') as f2:
    for i in newsLink:
        f2.write(i)