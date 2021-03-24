#!/usr/bin/python3

import sys

import translators
# from PyQt5.QtWidgets import QApplication
from mew_translator import mew_translator


translator = mew_translator()
# test = translator.translate_to_en("这是一个测试,主要为了测试输出和输入的误差")
# print(test)
# print(translator.translate_to_cn(test))


# print(translator._dict)
for key in translator._dict.keys():
    value = translator._dict[key]
    new_value = ""
    for char in value:
        if char == '.':
            new_value.join('呜')
        else:
            new_value.join('喵')
    translator._dict[key] = new_value
print(translator._dict)