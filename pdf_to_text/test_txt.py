import sys
from io import StringIO

from pdfminer.high_level import extract_text_to_fp


def main():
    output_string = StringIO()
    f = sys.argv[1]
    with open(f, 'rb') as fin:
        extract_text_to_fp(fin, output_string, maxpages=1)
    print(output_string.getvalue())


if __name__ == "__main__":
    main()
