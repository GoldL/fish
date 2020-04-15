# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 上午11:41
# @Author  : iGolden
# @Software: PyCharm


def is_isbn_or_key(word):
    # isbn13 13个0-9的数字组成
    # isbn10 10个0-9数字组成，含有一些'-'
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_q = word.replace('-', '')
    if '-' in word and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
