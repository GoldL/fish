# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 下午10:33
# @Author  : iGolden
# @Software: PyCharm
from collections import namedtuple

from app.view_models.book import BookViewModel

MyWish = namedtuple('MyWish', ['id', 'book', 'gifts_count'])


class MyWishes:
    def __init__(self, wishes_of_mine, gift_count_list):
        self.wishes = []

        self.__wishes_of_mine = wishes_of_mine
        self.__gift_count_list = gift_count_list
        self.wishes = self.__parse()

    def __parse(self):
        temp_wishes = []
        for wish in self.__wishes_of_mine:
            my_wish = self.__matching(wish)
            temp_wishes.append(my_wish)
        return temp_wishes

    def __matching(self, wish):
        count = 0
        for gift_count in self.__gift_count_list:
            if wish.isbn == gift_count['isbn']:
                count = gift_count['count']
        my_gift = MyWish(wish.id, BookViewModel(wish.book), count)
        return my_gift
