#!/usr/bin/python3

import sys

from PyQt5.QtWidgets import QApplication
from mew_translator import MewTranslator
from main_window import MainWindow


translator = MewTranslator()
# test = translator.translate_to_en("这是一个测试,主要为了测试输出和输入的误差")
# print(test)
# print(translator.translate_to_cn(test))
# print(translator._dict)

#
# generate the encode mew dict through Moss code
#
def generate_encode_dict():
    for key in translator._dict.keys():
        value = translator._dict[key]
        new_value = ""
        for char in value:
            if char == '.':
                new_value = new_value + "呜"
            else:
                new_value = new_value + '喵'
        translator._dict[key] = new_value
    print(translator._dict)

#
# generate the decode mew dict through encode dict
#
def generate_decode_dict():
    new_dict = {}
    for key in translator._encode_dict.keys():
        new_dict[translator._encode_dict[key]] = key
    print(new_dict)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())