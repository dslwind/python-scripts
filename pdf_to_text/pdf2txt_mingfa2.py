# coding=utf-8
import os
import sys
import time
from pdfminer.high_level import extract_text


def pdf2txt(infile):
    text = extract_text(infile)
    text1 = [s for s in text.split(sep='\n') if s]
    text2 = [s.strip() for s in text1 if len(s.strip()) > 4]

    doc_name = ''
    description = ['●Features VS Benefits']
    for i in range(len(text2)):
        if (text2[i].startswith('Zhaga') or text2[i].startswith('* Zhaga')
                or text2[i].startswith('Lum') or text2[i].startswith('Samsung')
                or text2[i].startswith('Seoul')
                or text2[i].startswith('Tridonic')):
            break

        if 'Φ' in text2[i]:
            dn = text2[i].split()
            if len(dn) > 2 and (dn[0] in dn[1]):
                dn = dn[1:]
            for j in dn:
                doc_name = doc_name + j + ' '

        # if text2[i].startswith('Features'):
        #     print('●Features VS Benefits')
        # else:
        print(text2[i])

        if text2[i].startswith('*'):
            tmp = text2[i].replace('* ', '■')
            if not text2[i + 1].startswith('*'):
                if not (text2[i + 1].startswith('Zhaga')
                        or text2[i + 1].startswith('Lum')
                        or text2[i + 1].startswith('Samsung')
                        or text2[i + 1].startswith('Seoul')
                        or text2[i + 1].startswith('Tridonic')):
                    tmp = tmp + ' ' + text2[i + 1]
            description.append(tmp)
            # print(tmp)

    print('----------复制开始----------')
    print('Datasheet')
    print(doc_name)
    # for i in doc_name:
    #     print(i, end=' ')
    # print()
    for d in description:
        print(d)

    model = []
    for s in text2:
        if s.startswith('Example:'):
            t = s.replace('Example:', '')
            if ' ' in t:
                t.replace(' ', '')

            if t.endswith('-B'):
                model.append(t[:-2])
                model.append(t)
                model.append(t.replace('B', 'C'))
                model.append(t.replace('B', 'Z'))

            else:
                if t.endswith(',2') or t.endswith('.2'):
                    t = t[:-2]
                    model.append(t[:-1] + '2')

                model.append(t[:-4])
                model.append(t)
                model.append(t.replace(t[-3:], 'C-1'))

            break
    for s in text2:
        if '#' in s:
            model.append(s)

    for m in sorted(model):
        print(m)
    # for m in model:
    #     print(m)

    prefix = ['0 ', '8 ', '5 ']
    for p in prefix:
        if p in doc_name:
            if 'for' in doc_name and doc_name.index('for') < doc_name.index('Φ'):
                print(doc_name[doc_name.index('for') + 4:doc_name.index('Φ')])
            else:
                print(doc_name[doc_name.index(p) + 2:doc_name.index('Φ')])

    # outfile = infile.replace('pdf','txt')
    # with open(outfile, 'w', encoding='utf-8') as f:
    #     for d in description:
    #         f.write(d+'\n')
    #     for m in model:
    #         f.write(m+'\n')


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
