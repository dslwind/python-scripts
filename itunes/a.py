import os

from bs4 import BeautifulSoup

albums = [f for f in os.listdir() if f.endswith('.html')]

for album in albums:
    fn = album.replace('html', 'txt')
    if os.path.exists(fn):
        continue

    htmlfile = open(album, 'r', encoding='utf-8')
    htmlhandle = htmlfile.read()

    soup = BeautifulSoup(htmlhandle, 'lxml')
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
            if t.endswith(' (Live)'):
                t = t[:-7]
            f.write(t + '\n')
