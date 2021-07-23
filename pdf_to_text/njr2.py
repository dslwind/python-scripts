# coding=utf-8
import os
import sys
import time

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer


def pdf2txt(f):

    model = set([])
    ext = ''
    ver = ''

    for page_layout in extract_pages(f):
        page1 = False
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                text = element.get_text()

                s = str(text).strip()
                if s == '- 1 -':
                    page1 = True
                    break
                # print(count, s)
                
                # if s.startswith('■ GENERAL DESCRIPTION'):
                #     ext = s
                if s.startswith('●'):
                    print(s.replace('● ', '■'))
                elif s.startswith('■'):
                    print(s.replace('■ ', '●'))
                else:
                    print(s)
                
                if s.startswith('NJ'):
                    if '\n' in s:
                        tmp = s.split('\n')
                        for i in tmp:
                            model.add(i.strip())
                    else:
                        model.add(s)
                if s.startswith('Ver.'):
                    if '\n' in s:
                        ver = s.replace('\n', '')
                    else:
                        ver = s
        if page1: break
                

    ext_list = ext.replace('■ ', '●').replace('● ',
                                              '■').replace('  ',
                                                           ' ').split('\n')
    ext_list = [i.strip() for i in ext_list if i.strip()]


    # print('Datasheet')
    # print('●GENERAL DESCRIPTION')
    # gen_des = ext_list[1:ext_list.index('●FEATURES')]
    # print('■'+' '.join(gen_des))
    # features = ext_list[ext_list.index('●FEATURES'):ext_list.index('●PIN CONFIGURATION')]
    # print('\n'.join(features))
    print('\n'.join(sorted(list(model))))
    print(ver)


def main():
    while True:
        files = set(os.listdir())
        time.sleep(5)
        new_file = set(os.listdir()) - files
        if new_file:
            print('发现新文件，提取信息……')
            f = list(new_file)[0]
            if f.endswith('.pdf'):
                pdf2txt(f)


if __name__ == "__main__":
    main()
