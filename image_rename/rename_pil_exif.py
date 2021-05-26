import os

from PIL import ExifTags, Image


def renameByExif(filename):
    with open(filename, 'rb') as f:
        img = Image.open(f)
        tags = {
            ExifTags.TAGS[k]: v
            for k, v in img._getexif().items()
            if k in ExifTags.TAGS
        }

    FIELD0 = 'DateTime'
    FIELD1 = 'DateTimeOriginal'
    FIELD2 = 'SubsecTimeOriginal'

    file_ext = os.path.splitext(filename)[1]

    if (FIELD1 not in tags) and (FIELD0 not in tags):
        print('No datetime info found')
        return

    if FIELD1 in tags:
        new_name = 'IMG_' + tags[FIELD1].replace(':', '').replace(' ', '_')
        if FIELD2 in tags:
            new_name = new_name + tags[FIELD2]

    elif FIELD0 in tags:
        new_name = 'IMG_' + tags[FIELD0].replace(':', '').replace(' ', '_')

    tot = 1
    while os.path.exists(new_name+file_ext):
        if tot == 1:
            new_name = new_name + '-' + str(tot)
        else:
            new_name = new_name.split('-')[0] + '-' + str(tot)
        tot += 1

    new_name2 = new_name + file_ext
    print(new_name2)
    os.rename(filename, new_name2)


valid_extensions = [".jpg", ".jpeg", ".png", ".JPG", "JPEG", ".PNG"]

for filename in os.listdir('.'):

    # Get the file extension
    file_ext = os.path.splitext(filename)[1]

    # If the file does not have a valid file extension
    # then skip it
    if file_ext in valid_extensions:
        print(filename)
        renameByExif(filename)
