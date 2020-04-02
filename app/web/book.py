# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 下午3:21
# @Author  : iGolden
# @Software: PyCharm
from flask import jsonify

from app.web.__inint__ import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q: 普通查询关键字 isbn
        page
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
