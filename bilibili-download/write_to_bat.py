from bs4 import BeautifulSoup

htmlfile = open('1.html', 'r', encoding='utf-8')
htmlhandle = htmlfile.read()

soup = BeautifulSoup(htmlhandle, 'lxml')
prefix = 'http'
suffix = ''
links = soup.find_all('a', class_='title')

# with open('videos.txt', 'w') as f:
#     for i in links:
#         f.write('https:' + i['href'] + '\n')

# with open('videos.txt', 'r') as f:
#     videos = f.readlines()

# with open('download.bat', 'w') as f:
#     for v in videos:
#         # print(['you-get', '-i', v[:-1]])
#         # subprocess.call(['you-get', v[:-1]])
#         f.write('you-get ' + v)

with open('download.bat', 'w') as f:
    for v in links:
        # print(['you-get', '-i', v[:-1]])
        # subprocess.call(['you-get', v[:-1]])
        f.write('you-get https:' + str(v['href']) + '\n')
