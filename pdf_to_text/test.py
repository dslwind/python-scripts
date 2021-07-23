# coding=utf-8

import sys
from pdfminer.high_level import extract_text

def pdf2txt(infile):
    text = extract_text(infile)
    text1 = [s for s in text.split(sep='\n') if s]
    text2 = [s.strip() for s in text1 if len(s.strip()) > 4]

    description = ['●Features VS Benefits']
    for i in range(len(text2)):
        if text2[i].startswith('Zhaga'):
            break

        if text2[i].startswith('*'):
            tmp = text2[i].replace('* ', '■')
            if not text2[i + 1].startswith('*'):
                tmp = tmp + text2[i + 1]
            description.append(tmp)

    model = []
    for s in text2:
        if s.startswith('Example:'):
            t = s.replace('Example:', '')
            model.append(t[:-4])
            model.append(t)
            model.append(t.replace(t[-3:], 'C-1'))
            break
    
    outfile = infile.replace('pdf','txt')
    with open(outfile, 'w', encoding='utf-8') as f:
        f.write(text2[1])
        for d in description:
            f.write(d+'\n')
        for m in model:
            f.write(m+'\n')

def main():
    pdf2txt(sys.argv[1])

if __name__ == "__main__":
    main()