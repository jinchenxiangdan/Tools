#!/usr/bin/python3

# import library
import translators as tl

class mew_translator():

    _translator = ''
    _dict = {}
    def __init__(self):
        # set default translator 
        self._translator = 'google'
        self._dict = {'a':'.-'  ,'b':'-...','c':'-.-.','d':'-..'  ,'e':'.'   ,
            'f':'..-.','g':'--.' ,'h':'....','i':'..'  ,'j':'.---',
            'k':'-.-' ,'l':'.-..','m':'--'  ,'n':'-.'  ,'o':'---' ,
            'p':'.--.','q':'--.-','r':'.-.' ,'s':'...' ,'t':'-'   ,
            'u':'..-' ,'v':'...-','w':'.--' ,'x':'-..-','y':'-.--','z':'--..',
            '0':'-----' ,'1':'.----' ,'2':'..---' ,'3': '...--','4': '....-' ,
            '5': '.....','6': '-....','7': '--...','8': '---..','9': '----.' }

    def translate_to_en(self, input:str) -> str:
        if self._translator == 'google':
            return (tl.google(input, if_use_cn_host=False, to_language='en'))
        if self._translator == 'bing':
            return (tl.bing(input, if_use_cn_host=False))
        else:
            print("Error: no translator claimed!")
    
    def translate_to_cn(self, input:str) -> str:
        if self._translator == 'google':
            return (tl.google(input, if_use_cn_host=False, to_language='zh-CN'))
        if self._translator == 'bing':
            return (tl.bing(input, if_use_cn_host=False, to_language='zh-CN'))
        else:
            print("Error: no translator claimed!")

    def encode_mew(self, input:str) -> str:
        x = '喵呜'
        output = ''
        for char in input:
            if char in self._dict:
                char = self._dict[char]
        return x
            