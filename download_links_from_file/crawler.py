import os

import requests
from bs4 import BeautifulSoup

proxies = {'http': 'http://127.0.0.1:1080', 'https': 'https://127.0.0.1:1080'}

url = 'https://private70.ghuws.win/htm_mob/8/1904/3496937.html'

r = requests.get(url, proxies=proxies)
data = r.text
soup = BeautifulSoup(data, 'lxml')

with open('l2.txt', 'w', encoding='utf-8') as f:
    f.write(str(soup))