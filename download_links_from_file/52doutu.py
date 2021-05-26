import os

import requests
from bs4 import BeautifulSoup

proxies = {'http': 'http://127.0.0.1:1080', 'https': 'https://127.0.0.1:1080'}

url = 'https://www.52doutu.cn/p/58/'

r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'lxml')

imgs = soup.findAll('img')
# print(imgs)
d = 'hanhan'
os.mkdir(d)

for i in range(1, len(imgs) - 1):
    s = str(imgs[i])
    link = s[(s.index('data-original') + 15):(s.index(' src') - 1)]

    fn = link.split('/')[-1]

    fn = os.path.join(d, fn)
    if os.path.exists(fn):
        continue
    ir = requests.get(link)
    print(fn)

    with open(fn, 'wb') as im:
        im.write(ir.content)
