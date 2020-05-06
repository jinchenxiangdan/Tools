# import portion
import pip
import sys
import os
try:
    import crossref_commons.retrieval
except ImportError as e:
    pip.main(['install', 'crossref-commons'])
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
#
# global
#
XML_TARGET_DIRECTORY    = "xml_outputs"
JSON_TARGET_DIRECTORY   = "json_outputs"
FILE_NOT_EXIST_ERROR    = -1
NO_ERROR                = 0

#
# write xml data to files (filename: [DOI].xml) according to input filename
#
def get_xml_metadata_from_file(filename):
    try:
        in_file = open(filename, 'r')
    except IOError as e:
        print(e)
        return FILE_NOT_EXIST_ERROR

    lines = in_file.readlines()
    create_target_directory()

    for line in lines:
        xml             = crossref_commons.retrieval.get_publication_as_xml(line.strip())
        line            = line.strip().replace("/", "-")
        file_name       = XML_TARGET_DIRECTORY + "/" +line + ".xml"
        tartget_file    = open(file_name, 'wb')
        xml_content     = ET.tostring(xml, encoding='utf8', method='xml')
        tartget_file.write(xml_content)

    return NO_ERROR


def create_target_directory():
    try:
        os.mkdir(XML_TARGET_DIRECTORY)
    except FileExistsError:
        pass
    # os.mkdir(JSON_TARGET_DIRECTORY)


#
# usage1 : python3 get_metadata_DOI.py [filename1, filename2 ...]
# usage2 : python3 get_metadata_DOI.py
#          >>> filename
#
def main():
    filename = ""
    if(len(sys.argv) <= 1):
        filename = input("Please input the file with DOI content: ")
        get_xml_metadata_from_file(filename)
    else:
        for filename in sys.argv:
            # try to open file
            try:
                in_file = open(filename, 'r')
            except IOError as e:
                print(e)
                exit(1)
            get_xml_metadata_from_file(filename)


if __name__ == "__main__":
    main()