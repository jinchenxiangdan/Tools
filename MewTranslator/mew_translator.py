#!/usr/bin/python3

# import library
import translators as tl

class MewTranslator():

    _translator = ''
    _encode_dict = {}
    def __init__(self):
        # set default translator 
        self._translator = 'google'
        self._encode_dict = {'a': '呜喵', 'b': '喵呜呜呜', 'c': '喵呜喵呜', 'd': '喵呜呜', 'e': '呜', 'f': '呜呜喵呜', 'g': '喵喵呜', 'h': '呜呜呜呜', 'i': '呜呜', 'j': '呜喵喵喵', 'k': '喵呜喵', 'l': '呜喵呜呜', 'm': '喵喵', 'n': '喵呜', 'o': '喵喵喵', 'p': '呜喵喵呜', 'q': '喵喵呜喵', 'r': '呜喵呜', 's': '呜呜呜', 't': '喵', 'u': '呜呜喵', 'v': '呜呜呜喵', 'w': '呜喵喵', 'x': '喵呜呜喵', 'y': '喵呜喵喵', 'z': '喵喵呜呜', '0': '喵喵喵喵喵', '1': '呜喵喵喵喵', '2': '呜呜喵喵喵', '3': '呜呜呜喵喵', '4': '呜呜呜呜喵', '5': '呜呜呜呜呜', '6': '喵呜呜呜呜', '7': '喵喵呜呜呜', '8': '喵喵喵呜呜', '9': '喵喵喵喵呜'}

        self._decode_dict = {'呜喵': 'a', '喵呜呜呜': 'b', '喵呜喵呜': 'c', '喵呜呜': 'd', '呜': 'e', '呜呜喵呜': 'f', '喵喵呜': 'g', '呜呜呜呜': 'h', '呜呜': 'i', '呜喵喵喵': 'j', '喵呜喵': 'k', '呜喵呜呜': 'l', '喵喵': 'm', '喵呜': 'n', '喵喵喵': 'o', '呜喵喵呜': 'p', '喵喵呜喵': 'q', '呜喵呜': 'r', '呜呜呜': 's', '喵': 't', '呜呜喵': 'u', '呜呜呜喵': 'v', '呜喵喵': 'w', '喵呜呜喵': 'x', '喵呜喵喵': 'y', '喵喵呜呜': 'z', '喵喵喵喵喵': '0', '呜喵喵喵喵': '1', '呜呜喵喵喵': '2', '呜呜呜喵喵': '3', '呜呜呜呜喵': '4', '呜呜呜呜呜': '5', '喵呜呜呜呜': '6', '喵喵呜呜呜': '7', '喵喵喵呜呜': '8', '喵喵喵喵呜': '9'}

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
        output = ''
        for char in input:
            if char in self._encode_dict:
                output = output + self._encode_dict[char]
        assert len(output) == len(input)
        return output

    def decode_mew(self, input:str) -> str:
        output = ''
        for char in input:
            if char in self._decode_dict:
                output = output + self._decode_dict[char]
        assert len(output) == len(input)
        return output
            