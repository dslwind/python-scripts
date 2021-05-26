from bs4 import BeautifulSoup

with open('album.html', 'r', encoding='utf-8') as hf:
    htmlhandle = hf.read()
    soup = BeautifulSoup(htmlhandle, 'lxml')

a = soup.find_all('a')
with open('albums.txt', 'w', encoding='utf-8') as f:
    for i in a:
        a_url = i.attrs['href']
        f.write(a_url+'\n')