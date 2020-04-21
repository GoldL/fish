# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 上午11:15
# @Author  : iGolden
# @Software: PyCharm


class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages']
        self.author = '、'.join(book['author'])
        self.price = book['price']
        self.summary = book['summary']
        self.isbn = book['isbn']
        self.image = book['image']

    @property
    def intro(self):
        intro = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return '/'.join(intro)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.keyword = ''
        self.books = []

    def fill(self, yushu_book, keyword):
        self.keyword = keyword
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
