# coding=utf-8

import sys

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer


def remove_blank(s):
    t = ''
    for i in s.split('\n'):
        if i.strip():
            i = ' '.join(i.split())
            if i[0].islower():
                t = t + i
            else:
                t = t + '\n' + i

    return t.strip()


def pdf2txt(f):

    for page_layout in extract_pages(f, page_numbers=[0]):

        count = 1
        text_area = []
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                text = element.get_text()

                s = str(text).strip()
                if s:
                    text_height = round(element.height)
                    x0 = round(element.x0)
                    y1 = -round(element.y1)
                    text_area.append([y1, x0, text_height, s])

                    # print('[', count, y1, x0, text_height, ']', s)
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

        return text_area, text


def main():
    if len(sys.argv) == 2:
        f = sys.argv[1]
        if f.endswith('.pdf'):
            _, text = pdf2txt(f)
            print('\n'.join(text))
        else:
            print('Error: not a PDF file')
    else:
        print('Usage: python pdf_to_txt.py input.pdf')


if __name__ == "__main__":
    main()
