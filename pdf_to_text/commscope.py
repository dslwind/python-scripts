# coding=utf-8
import os
import sys
import time

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer


def remove_blank(s):
    return ' '.join(s.split())


def extract(f):
    for page_layout in extract_pages(f):

        text_area = []
        count = 1

        for element in page_layout:
            if isinstance(element, LTTextContainer):
                text = element.get_text()
                s = str(text).strip()
                text_height = round(element.height)
                x0 = round(element.x0)
                y1 = -round(element.y1)
                # print(count, y1, x0, text_height, s)
                text_area.append([y1, x0, text_height, s])
                count += 1

        break

    text_area.sort()
    # print(text_area)

    product_type = []
    text = [
        remove_blank(text_area[0][-1]),
        remove_blank(text_area[1][-1]),
    ]
    model = [text[0]]
    doc_name = text[0]

    if '|' in text[0]:
        t = text[0].split('|')
        model = [i.strip() for i in t]
        doc_name = text[0].replace(' | ', ' ')
    product_type.append(text[1].split(',')[0])

    i = 2
    if not text_area[2][2] == 14:
        s = text_area[2][-1]
        sl = s.split('\n')
        t = sl[0]
        for l in sl[1:]:
            if l[0].islower():
                t = t + ' ' + l
            else:
                t = t + '\n■' + l
        s = '■' + t.replace('  ', ' ')
        text.append(s)
        i = 3

    while i < len(text_area):
        j = i + 1
        s = remove_blank(text_area[i][-1])

        if text_area[i][2] == 14:
            s = '●' + s
        elif text_area[i][2] == 9:
            s = '■' + s

        while j < len(text_area) and text_area[i][0] == text_area[j][0]:
            t = remove_blank(text_area[j][-1])
            if text_area[i][2] == 9:
                s = s + ': ' + t
            else:
                s = s + ' ' + t

            if s.startswith('■Product Type'):
                product_type.append(t)

            if s.startswith('■Product Series'):
                if product_type[0].startswith(t):
                    product_type[0] = product_type[0][len(t) + 1:]

            j += 1

        text.append(s)
        i = j

    i = 0
    while i < len(text) - 2:
        s = text[i]
        if s.startswith('■Regional Availability'):
            text.remove(text[i])
            break
        i += 1

    i = 2
    while i < len(text) - 2 and not text[i].startswith('●General'):
        i += 1
    i += 1
    while i < len(text) - 2 and not text[i].startswith('●'):
        i += 1

    date = text[-1][text[-1].index(':') + 2:]

    des = ''
    if text_area[1][2] == 13:
        doc_name = doc_name + ' ' + text[1]
    else:
        des = '●' + text[1]
        doc_name = doc_name + ' ' + product_type[1]

    print('--------复制开始--------')
    print('Datasheet')
    print(doc_name)
    if des:
        print(des)
    print('\n'.join(text[2:i]))
    print('\n'.join(model))
    print(';'.join(product_type))
    print(date)


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
