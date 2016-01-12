# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import requests


s = requests.Session()

url = 'http://www.nicovideo.jp/watch/sm15022913/videoExplorer'
r = s.get('https://marco.ms.dendai.ac.jp/PTDU79130R/AX0101.aspx')
soup = BeautifulSoup(r.text)
