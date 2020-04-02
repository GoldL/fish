# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 下午3:56
# @Author  : iGolden
# @Software: PyCharm
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
from app.web import user