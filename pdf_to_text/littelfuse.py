import os
import time

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer


def remove_blank(s):
    t = ''
    for i in s.split('\n'):
        if i.strip():
            i = ' '.join(i.split())
            if i[0].islower() or i[0].isdigit():
                t = t + ' ' + i
            else:
                t = t + '\n' + i

    return t.strip()


def extract(f):

    for page_layout in extract_pages(f, page_numbers=[0]):

        count = 1
        text_area = []
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                text = element.get_text()

                s = str(text).strip()
                if s:
                    text_height = round(element.height)
                    text_width  = round(element.width)
                    x0 = round(element.x0)
                    y1 = -round(element.y1)
                    text_area.append([y1, x0, text_height, s])

                    # print('[', count, y1, x0, text_height, text_width, ']', s)
                    # print(s)
                    count += 1

        # text_area.sort()
        text = []

        i = 0
        while i < len(text_area):
            j = i + 1
            s = remove_blank(text_area[i][-1])
            while j < len(text_area) and text_area[i][0] == text_area[j][0]:
                t = remove_blank(text_area[j][-1])
                s = s + '\t' + t
                j += 1
            text.append(s)
            i = j

        # print('\n'.join(text))

        # return text_area, text
        return (text)


def fuse(text):

    i = 0
    while i < len(text) and not text[i].startswith('Description'):
        i += 1
    # print(text[i])
    des = []
    while i < len(text) and not text[i].startswith('Features'):
        des.append(text[i])
        i += 1

    d = remove_blank('\n'.join(des))
    # print(d)
    d = '●' + d.replace('\n', '\n■')
    print(d)

    features = []
    while i < len(text) and not text[i].startswith('App'):
        features.append(text[i])
        i += 1

    feature = remove_blank('\n'.join(features))
    feature = '●' + feature.replace('■ ', '■').replace('• ', '■')
    print(feature)


def main():
    while True:
        files = set(os.listdir())
        time.sleep(3)
        new_file = set(os.listdir()) - files
        if new_file:
            f = list(new_file)[0]
            if f.endswith('.pdf'):
                print('发现新文件，提取信息……')
                fuse(extract(f))


if __name__ == "__main__":
    main()
