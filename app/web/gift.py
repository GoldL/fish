from flask import current_app, flash, render_template, redirect, url_for

from app.models.base import db
from app.models.gift import Gift
from app.web.__inint__ import web
from flask_login import login_required, current_user

__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    pass


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('这本书已添加至你的赠送清单或已存在你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
