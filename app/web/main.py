from app.web.__inint__ import web

__author__ = '七月'


@web.route('/')
def index():
    return 'hello'


@web.route('/personal')
def personal_center():
    pass
