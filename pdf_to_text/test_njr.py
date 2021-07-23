import os
import sys

import requests
from bs4 import BeautifulSoup, element

url = 'https://www.njr.com/electronic_device/products/NJW1280.html'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'lxml')

content = soup.find(id="entry-detail")

text = []
for i in list(content.descendants):
    if isinstance(i, element.NavigableString) and i.string.strip():
        text.append(i.string.strip())


gen_des = ['●General Description']
tmp = text[text.index('General Description') + 1:text.index('Applications')]
gen_des.extend(['■' + i.strip() + '.' for j in tmp for i in j.split('.') if i])


features = ['●Features']
tmp = text[text.index('Features') + 1:text.index('General Description')]
for i in tmp:
    if i.startswith('-'):
        features.append('▲' + i)
    else:
        features.append('■' + i)


applications = []
tmp = text[text.index('Applications') + 1:text.index('Related Data')]
gen_des.extend(['■' + i.strip() + '.' for i in tmp if i])