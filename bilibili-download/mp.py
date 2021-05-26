from multiprocessing import Pool
import subprocess


def download(v):
    subprocess.call(['you-get', v[:-1], '-o', 'BiliVideoDownload/李子柒'])


if __name__ == "__main__":
    pool = Pool(processes=8)
    with open('videos.txt', 'r') as f:
        videos = f.readlines()

    for v in videos:
        pool.apply_async(download, args=(v, ))
    print('======  apply_async  ======')
    pool.close()
    pool.join()
