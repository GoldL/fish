# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 下午3:21
# @Author  : iGolden
# @Software: PyCharm
from flask import jsonify, request
from app.web.__inint__ import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from app.forms.book import SearchForm


@web.route('/book/search')
def search():
    """
        q: 普通查询关键字 isbn
        page
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)
