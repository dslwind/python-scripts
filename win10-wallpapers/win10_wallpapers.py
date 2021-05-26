import glob
import os
import shutil
import time

from PIL import Image, ImageChops

# target = r'{}\pictures\wallpapers_auto'.format(os.environ.get('USERPROFILE'))
target = 'images'
user = os.environ.get('localappdata')
source_path = r"{}\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets".format(
    user)
target_path = os.path.abspath(target)


# 壁纸提取
def wall_save():
    '''壁纸保存'''
    if os.path.exists(source_path):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        tot = 1
        num_wall = 0
        for root, dirs, files in os.walk(source_path):
            for file in files:
                # 构建文件地址
                src_file = os.path.join(root, file)
                # 这里要用try expect 否则会报OSError
                try:
                    if os.path.isfile(src_file):
                        # 判断分辨率 过滤图标
                        img = Image.open(src_file)
                        w, h = img.size
                        if (w >= 1920 and h >= 1080) or (w >= 1080
                                                         and h >= 1920):
                            shutil.copy(src_file, target_path)
                            num_wall = num_wall + 1
                except (OSError, NameError):
                    # print('异常{}张（图标不用理会）'.format(tot))
                    tot = tot + 1
    print('本次提取{}张'.format(num_wall))
    '''文件重命名'''
    # 列出文件下所有文件
    filelist = os.listdir(target)
    t = int(time.time())
    num = 1
    for filename in filelist:
        os.chdir(target)  #切换工作路径,path为需要处理的数据所在的目录
        os.rename(filename, (str(t + num) + '.jpg'))
        num = num + 1
    print('重命名ok')


# source_path 创建生成器
def source_gen():
    for root, dirs, files in os.walk(source_path):
        for file in files:
            source_src_file = os.path.join(root, file)
            try:
                if os.path.isfile(source_src_file):
                    img = Image.open(source_src_file)
                    w, h = img.size
                    if (w >= 1920 and h >= 1080) or (w >= 1080 and h >= 1920):
                        yield source_src_file
            except (OSError, NameError):
                pass


# target_path 创建生成器
def target_gen():
    for root, dirs, files, in os.walk(target):
        for file in files:
            target_src_file = os.path.join(root, file)
            yield target_src_file


# 壁纸更新
def wall_updata():
    same_list = []
    source_list = []
    for source_file in source_gen():
        source_list.append(source_file)
        image_one = Image.open(source_file)
        for target_file in target_gen():
            image_two = Image.open(target_file)
            diff = ImageChops.difference(image_one, image_two)
            if diff.getbbox() is None:
                same_list.append(source_file)
                # shutil.copy(source_file, target_path)
    diff_list = set(source_list).difference(same_list)
    wall_num = len(diff_list)
    for file in diff_list:
        shutil.copy(file, target_path)
    if wall_num == 0:
        print('啊！微软又偷懒！没更新哦')
    else:
        print("本次更新{}张".format(wall_num))
    if wall_num != 0:
        filelist = os.listdir(target)
        t = int(time.time())
        salt_num = 1
        for filename in filelist:
            # 筛选没有命名的进行命名
            if filename.endswith('.jpg') != True:
                os.chdir(target_path)  #切换工作路径,path为需要处理的数据所在的目录
                os.rename(filename, (str(t + salt_num) + '.jpg'))
                salt_num = salt_num + 1
        print('重命名OK！')


# run
def start():
    if not os.path.exists(target_path):
        print('目标文件夹不存在——提取壁纸')
        os.makedirs(target_path)
        wall_save()
    else:
        print('updating......')
        source_gen()
        wall_updata()


if __name__ == "__main__":
    start()
    input('按任意键退出')
