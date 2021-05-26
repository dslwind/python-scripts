import re
import sys
import time
import urllib

import requests
from bs4 import BeautifulSoup

proxy = {
    'http': 'http://127.0.0.1:1080',
    'https': 'https://127.0.0.1:1080'
}

host = 'https://mojim.com'
singer_urls = {'http://mojim.com/cnh100111-A1.htm',
               'http://mojim.com/cnh100111-A1-1.htm'}

lyricist = '林夕'
song_names = set([])
rub = ['<br/>', '\n', '更多更详尽歌词 在 ※ Mojim.com\u3000魔镜歌词网 ',
       '<dt class="fsZx2" id="fsZx2">\n</dt>', '<ol><li>\n</li></ol>', '\n陈奕迅\n']

f = open('eason_linxi.txt', 'w', encoding='utf8')

for singer_url in singer_urls:
    req = requests.get(singer_url, proxies=proxy)
    data = req.text
    soup = BeautifulSoup(data, 'lxml')

    songlist = soup.find_all(class_='hb3')
    for i in songlist:
        if (i.find(class_='hc2', text=lyricist)):
            lrc_url = host + i.find('a')['href']
        else:
            continue

        req = requests.get(lrc_url, proxies=proxy)
        data = req.text
        soup = BeautifulSoup(data, "html.parser")

        song_name = soup.find(text=re.compile("var songname")).string.split(';')[
            0].replace('var songname=', '').replace('\"', '')
        if song_name in song_names:
            continue
        song_names.add(song_name)

        a = soup.find(class_='fsZx1')
        if a == None:
            continue
        a = [str(i) for i in a]

        for i in rub:
            while i in a:
                a.remove(i)

        lrc = ''
        for i in a:
            if i.startswith('[') or i.startswith('<ol>'):
                continue
            lrc += i
            lrc += '\n'

        print('正在写入歌曲：', song_name)

        f.write(lrc)

f.close()