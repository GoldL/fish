# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 下午3:56
# @Author  : iGolden
# @Software: PyCharm
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.__inint__ import web
    app.register_blueprint(web)
