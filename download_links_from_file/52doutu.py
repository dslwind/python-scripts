import os
import sys
import requests
from bs4 import BeautifulSoup


def extract_imgs(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    imgs = soup.findAll('img')
    print('%d images found.' % len(imgs))
    return imgs


def download(imgs, dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
    for i in range(1, len(imgs) - 1):
        s = str(imgs[i])
        link = s[(s.index('data-original') + 15):(s.index(' src') - 1)]
        fn = link.split('/')[-1]
        fn = os.path.join(dir, fn)
        if os.path.exists(fn):
            print('File aleady exists, skipping download.')
            continue
        ir = requests.get(link)
        print(fn)
        with open(fn, 'wb') as im:
            im.write(ir.content)


def main(argv):
    # url = 'https://www.52doutu.cn/p/58'
    imgs = extract_imgs(argv[1])
    download(imgs, argv[2])


if __name__ == "__main__":
    main(sys.argv)