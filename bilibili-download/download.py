with open('videos.txt', 'r') as f:
    videos = f.readlines()

with open('download.bat', 'w') as f:
    for v in videos:
        # print(['you-get', '-i', v[:-1]])
        # subprocess.call(['you-get', v[:-1]])
        f.write('you-get ' + v)
