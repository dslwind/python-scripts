import os
import time


def timestamp_to_date(time_stamp, format_string="%Y%m%d_%H%M%S"):
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date


for filename in os.listdir('.'):
    print(filename)
    if not filename == 'rename.py' and os.path.isfile(filename):
        if filename.endswith('.jpg'):
            new_name = 'IMG_' + \
                timestamp_to_date(int(filename[:-4])/1000) + filename[-7:]
            os.rename(filename, new_name)
        elif filename.endswith('.jpeg'):
            new_name = 'IMG_' + \
                timestamp_to_date(int(filename[:-5])/1000) + filename[-8:]
            os.rename(filename, new_name)

