from PIL import ExifTags
from PIL import Image

img = Image.open('test.jpg')


def read_exif(img):

    exif_data = img._getexif()

    # This should give you a dictionary indexed by EXIF numeric tags.
    # If you want the dictionary indexed by the actual EXIF tag name strings,
    # try something like:

    exif = {
        ExifTags.TAGS[k]: v
        for k, v in exif_data.items() if k in ExifTags.TAGS
    }

    return exif


def exif_tags(filename):
    from PIL import ExifTags
    from PIL import Image

    with open(filename, 'rb') as f:
        img = Image.open(f)
        tags = {
            ExifTags.TAGS[k]: v
            for k, v in img._getexif().items() if k in ExifTags.TAGS
        }
    return tags
