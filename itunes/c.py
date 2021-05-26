import os

import requests
from bs4 import BeautifulSoup

proxies = {'http': 'http://127.0.0.1:1080', 'https': 'https://127.0.0.1:1080'}

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

with open('albums.txt', 'r', encoding='utf-8') as f:
    urls = f.readlines()

for url in urls:
    fn = url[34:].strip('\n').replace('/', '_') + '.txt'
    if os.path.exists(fn):
        continue

    req = requests.get(url.strip(), proxies=proxies, headers=headers)
    data = req.text
    soup = BeautifulSoup(data, "lxml")

    album_name = soup.find(class_='product-header__title').string
    artist = soup.find(
        class_="product-header__identity album-header__identity").text.strip()
    genre = soup.find(class_="product-header__list__item").a.text
    album_date = soup.find(class_="link-list__item__date").text
    album_copyright = soup.find(class_="link-list__item--copyright").text

    songs = soup.find_all(class_='table__row__headline')
    title = [i.string.strip() for i in songs]

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(album_name + '\n')
        f.write(artist + '\n')
        f.write(genre + '\n')
        f.write(album_date + '\n')
        f.write(album_copyright + '\n')
        f.writelines('\n')

        for t in title:
            if t.endswith(' (Live)') or t.endswith(' [Live]'):
                t = t[:-7]
            f.write(t + '\n')
