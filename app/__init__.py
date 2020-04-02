# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 下午3:56
# @Author  : iGolden
# @Software: PyCharm
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.__inint__ import web
    app.register_blueprint(web)