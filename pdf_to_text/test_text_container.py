# coding=utf-8
import os
import sys
import time

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer


def extract(f):
    for page_layout in extract_pages(f, maxpages=1):
        count = 0
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                text = element.get_text()
                s = str(text).strip()
                print(s)


def main():
    while True:
        files = set(os.listdir())
        time.sleep(5)
        new_file = set(os.listdir()) - files
        if new_file:
            f = list(new_file)[0]
            if f.endswith('.pdf'):
                print('发现新文件，提取信息……')
                extract(f)


if __name__ == "__main__":
    main()
