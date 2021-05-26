import subprocess
from multiprocessing import Pool

from bs4 import BeautifulSoup

htmlfile = open('1.html', 'r', encoding='utf-8')
htmlhandle = htmlfile.read()

soup = BeautifulSoup(htmlhandle, 'lxml')
links = soup.find_all('a', class_='title')


def download(v):
    subprocess.call(['you-get', v, '-o', 'BiliVideoDownload'])


if __name__ == "__main__":
    pool = Pool(processes=8)

    for i in links:
        v = 'https:' + i['href']
        pool.apply_async(download, args=(v, ))
    print('======  apply_async  ======')
    pool.close()
    pool.join()
