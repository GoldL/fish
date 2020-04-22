# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 下午3:21
# @Author  : iGolden
# @Software: PyCharm

from flask import request, flash, render_template
from flask_login import current_user

from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.book import BookCollection, BookViewModel
from app.web.__inint__ import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from app.view_models.trade import TradeInfo


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
    # 书籍详情
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    has_in_gifts = False
    has_in_wishes = False

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template("book_detail.html", book=book, wishes=trade_wishes_model, gifts=trade_gifts_model,
                           has_in_wishes=has_in_wishes, has_in_gifts=has_in_gifts)
