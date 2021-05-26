import os

import requests
from bs4 import BeautifulSoup

proxies = {'http': 'http://127.0.0.1:1080', 'https': 'https://127.0.0.1:1080'}

# url = 'http://private70.ghuws.win/htm_mob/7/1810/3324604.html'
# url = 'http://private70.ghuws.win/htm_mob/16/1812/3360098.html'
# url = 'https://private70.ghuws.win/htm_mob/7/1810/3321856.html'
# url = 'https://t66y.com/htm_mob/7/1811/3357002.html'
# url = 'http://t66y.com/htm_mob/7/1904/3485374.html'
# url = 'https://private70.ghuws.win/htm_mob/8/1904/3496937.html'
# url = 'http://t66y.com/htm_mob/1908/7/3606588.html'
# url = 'https://www.52doutu.cn/p/72/'
url = 'http://t66y.com/htm_data/2007/16/4001022.html'

r = requests.get(url, proxies=proxies)
data = r.text
soup = BeautifulSoup(data, 'lxml')

imgs = soup.findAll('img')
print(imgs)
d = 'dx'
os.mkdir(d)

for i in imgs:
    s = str(i)
    link = s[s.index('data-src') + 10:-3]

    fn = link.split('/')[-1]

    fn = os.path.join(d, fn)
    if os.path.exists(fn):
        continue
    ir = requests.get(link, proxies=proxies)
    print(fn)

    with open(fn, 'wb') as im:
        im.write(ir.content)
