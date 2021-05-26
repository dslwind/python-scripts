# -*- coding: utf-8 -*-


def txt2asx():
    FileHandle = open("in.txt", "r")
    TvFile = open("out.asx", "w")
    FileList = FileHandle.readlines()

    TvFile.write('<asx version = "3.0" >\n')

    for File in FileList:
        File = File.replace('\n', '')
        position = File.index(',')
        title = File[:position]
        url = File[position + 1:]
        url = url.replace('&', r'&')

        entry = '\t<entry>\n\t\t<title>{0}</title>\n\t\t<ref href = "{1}"/>\n\t</entry>'.format(
            title, url)
        TvFile.write(entry + '\n')

    TvFile.write('</asx>')
    FileHandle.close()
    TvFile.close()
    print("Finished.")


if __name__ == '__main__':
    txt2asx()
