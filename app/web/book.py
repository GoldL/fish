# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 下午3:21
# @Author  : iGolden
# @Software: PyCharm

from flask import request, flash, render_template

from app.view_models.book import BookCollection
from app.web.__inint__ import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm


@web.route('/book/search')
def search():
    """
        q: 普通查询关键字 isbn
        page
    """
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)
        books.fill(yushu_book, q)
    else:
        flash("搜索的关键字不符合要求，请重新输入关键字")
    return render_template("search_result.html", books=books)


@web.route("/book/<isbn>/detail")
def book_detail(isbn):
    pass
