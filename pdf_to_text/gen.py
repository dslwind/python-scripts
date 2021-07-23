# coding=utf-8
import math
import os
import sys
import time

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer


def remove_blank(s):
    t = ''
    for i in s.split('\n'):
        if i.strip():
            i = ' '.join(i.split())
            if i[0].islower():
                t = t + ' ' + i
            else:
                t = t + '\n' + i

    return t.strip()


def extract(f):
    for page_layout in extract_pages(f, maxpages=1):
        text_area = []
        count = 1
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                text = element.get_text()

                s = str(text).strip()
                # s = ' '.join(s.split())
                text_height = round(element.height)
                x0 = round(element.x0)
                y1 = -round(element.y1)
                # print(count, y1, x0, text_height, s)
                text_area.append([y1, x0, text_height, s])
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

    print('\n'.join(text))


def main():
    while True:
        files = set(os.listdir())
        time.sleep(3)
        new_file = set(os.listdir()) - files
        if new_file:
            f = list(new_file)[0]
            if f.endswith('.pdf'):
                print('发现新文件，提取信息……')
                extract(f)


if __name__ == "__main__":
    main()
