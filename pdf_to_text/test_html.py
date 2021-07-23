from io import StringIO
from pdfminer.layout import LAParams
from pdfminer.high_level import extract_text_to_fp
output_string = StringIO()
with open('1.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string, laparams=LAParams(),
                       output_type='html', codec=None)
