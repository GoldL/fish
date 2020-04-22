# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 下午11:38
# @Author  : iGolden
# @Software: PyCharm
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer
from contextlib import contextmanager


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attr(self, attr_dic):
        for key, value in attr_dic.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
