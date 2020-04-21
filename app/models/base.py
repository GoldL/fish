# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 下午11:38
# @Author  : iGolden
# @Software: PyCharm

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)

    def set_attr(self, attr_dic):
        for key, value in attr_dic.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
