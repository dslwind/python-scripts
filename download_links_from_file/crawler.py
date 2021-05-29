import os

import requests
from bs4 import BeautifulSoup

proxies = {'http': 'http://127.0.0.1:7890', 'https': 'https://127.0.0.1:7890'}

url = 'https://www.52doutu.cn/p/58/'

r = requests.get(url, proxies=proxies)
data = r.text
soup = BeautifulSoup(data, 'lxml')

with open('l.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))