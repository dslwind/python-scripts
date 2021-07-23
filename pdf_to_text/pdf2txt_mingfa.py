# coding=utf-8

import sys
from pdfminer.high_level import extract_text


def pdf2txt(infile):
    text = extract_text(infile)
    text1 = [s for s in text.split(sep='\n') if s]
    text2 = [s.strip() for s in text1 if len(s.strip()) > 4]

    doc_name = ''
    description = ['●Features VS Benefits']
    for i in range(len(text2)):
        if text2[i].startswith('Zhaga') or text2[i].startswith('* Zhaga'):
            break

        if 'Φ' in text2[i]:
            doc_name = text2[i]

        # if text2[i].startswith('Features'):
        #     print('●Features VS Benefits')
        # else:
        print(text2[i])

        if text2[i].startswith('*'):
            tmp = text2[i].replace('* ', '■')
            if not text2[i + 1].startswith('*'):
                if not text2[i + 1].startswith('Zhaga'):
                    tmp = tmp + ' ' + text2[i + 1]
            description.append(tmp)
            # print(tmp)

    print('----------分割线----------')
    print('Datasheet')
    print(doc_name)
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
                if t.endswith(',2'):
                    t = t[:-2]
                    model.append(t[:-1]+'2')

                model.append(t[:-4])
                model.append(t)
                model.append(t.replace(t[-3:], 'C-1'))

            break

    for m in sorted(model):
        print(m)

    print(doc_name[doc_name.index('0 ')+2:doc_name.index('Φ')])

    # outfile = infile.replace('pdf','txt')
    # with open(outfile, 'w', encoding='utf-8') as f:
    #     for d in description:
    #         f.write(d+'\n')
    #     for m in model:
    #         f.write(m+'\n')


def main():
    pdf2txt(sys.argv[1])


if __name__ == "__main__":
    main()