import requests
import os

proxies = {'http': 'http://127.0.0.1:7890', 'https': 'https://127.0.0.1:7890'}

with open('a1.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        fn = line.split('/')[-1]
        fn = os.path.join('test', fn)

        if os.path.exists(fn):
            continue
        ir = requests.get(line, proxies=proxies)
        print(fn)

        with open(fn, 'wb') as im:
            im.write(ir.content)
