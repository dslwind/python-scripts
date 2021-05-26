from bs4 import BeautifulSoup

htmlfile = open('1.html', 'r', encoding='utf-8')
htmlhandle = htmlfile.read()

soup = BeautifulSoup(htmlhandle, 'lxml')
prefix = 'http'
suffix = ''
links = soup.find_all('a', class_='title')

with open('videos.txt', 'w') as f:
    for i in links:
        f.write('https:' + i['href'] + '\n')
