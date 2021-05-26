from __future__ import print_function

import os
import time
import exifread


def getExif(filename):
    FIELD1 = 'EXIF DateTimeOriginal'
    FIELD2 = 'EXIF SubSecTimeOriginal'
    with open(filename, 'rb') as f:
        tags = exifread.process_file(f)

    if FIELD1 in tags:
        new_name = 'IMG_' + str(tags[FIELD1]).replace(':', '').replace(
            ' ', '_') + str(tags[FIELD2])[:3] + os.path.splitext(filename)[1]
        os.rename(filename, new_name)

        # tot = 1

        # while os.path.exists(new_name):
        #     new_name = 'IMG_' + str(tags[FIELD1]).replace(':', '').replace(
        #         ' ', '_') + str(tags[FIELD2]) + '_' + str(tot) + os.path.splitext(filename)[1]
        #     tot += 1

        # new_name2 = new_name.split(".")[0] + os.path.splitext(filename)[1]
        # print(new_name2)
        # os.rename(filename, new_name2)
    else:
        print('No {} found'.format(FIELD1))
        state = os.stat(filename)
        time.strftime("%Y%m%d_%H%M%S", time.localtime(state[-2]))


for filename in os.listdir('.'):
    print(filename)
    if not filename.endswith('py') and os.path.isfile(filename):
        getExif(filename)
