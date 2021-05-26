# -*- coding: utf-8 -*-


def txt2asx():
    FileHandle = open("in2.txt", "r")
    TvFile = open("out.asx", "w")
    FileList = FileHandle.readlines()

    TvFile.write('<asx version = "3.0" >\n')
    i = 0
    while (i < len(FileList) - 1):
        title = FileList[i].replace('\n', '')
        url = FileList[i + 1].replace('\n', '')

        entry = '\t<entry>\n\t\t<title>{0}</title>\n\t\t<ref href = "{1}"/>\n\t</entry>'.format(
            title, url)
        TvFile.write(entry + '\n')

        i += 2

    TvFile.write('</asx>')
    FileHandle.close()
    TvFile.close()
    print("Finished.")


if __name__ == '__main__':
    txt2asx()
