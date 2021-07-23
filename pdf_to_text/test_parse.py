import sys
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def parse_pdf(infile):
    output_string = StringIO()
    with open(infile, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    # with open(infile[:-3]+'txt', 'w', encoding='utf-8') as f:
    #     f.write(output_string.getvalue())

    return output_string.getvalue()


def main():
    if len(sys.argv) == 2:
        f = sys.argv[1]
        if f.endswith('.pdf'):
            print(parse_pdf(f))
        else:
            print('Error: not a PDF file')
    else:
        print('Usage: python pdf_to_txt.py input.pdf')


if __name__ == "__main__":
    main()
