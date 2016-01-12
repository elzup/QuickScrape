# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import requests


s = requests.Session()

url = 'http://www.nicovideo.jp/mylist/7975931'
r = s.get(url)
soup = BeautifulSoup(r.text)
print(soup)
elems = soup.find(id='SYS_page_items').children()
# print(elems)

