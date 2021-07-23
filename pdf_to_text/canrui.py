import os
import sys
import time
from io import StringIO

from pdfminer.high_level import extract_text_to_fp


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
    output_string = StringIO()

    with open(f, 'rb') as fin:
        extract_text_to_fp(fin, output_string, maxpages=1)

    s = output_string.getvalue()
    t = s.replace('\uf06e ', '\n●').replace('\uf06c ', '\n■')
    t = t.replace('General Description ', 'General Description \n■')
    t = t.replace(' ◼ ', '\n●').replace(' ⚫ ', '\n■')
    t = remove_blank(t)

    tl = t.split('\n')
    tl[0] = tl[0]
    tl0 = tl[0].split()
    tl0 = tl[0][:tl[0].index('OCS')]
    tl0 = tl0.split()

    i = 0
    while i < len(tl0) and not tl0[i].startswith('Ver'):
        i += 1
    if tl0[i + 1][0].isupper():
        ver = tl0[i]
    else:
        ver = tl0[i] + tl0[i + 1]
        i = i + 1

    date = tl0[i + 1:i + 3]
    doc_name = tl0[i + 3:]

    if '●General Description' in tl:
        des_i = tl.index('●General Description')
    elif '●概述' in tl:
        des_i = tl.index('●概述')
    else:
        des_i = 1

    app = []
    if '●Applications' in tl:
        des = tl[des_i:tl.index('●Applications')]
        app = tl[tl.index('●Applications') + 1:]
    else:
        des = tl[des_i:]

    i = 0
    while i < len(app) and app[i].startswith('■'):
        i += 1
    app = app[:i]
    app = ';'.join(app).replace('■', '')

    print('Datasheet')
    print(' '.join(doc_name))
    # print(tl[0])
    print('\n'.join(des))
    print(app)
    print(' '.join(date))
    print(ver)


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
