# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 下午11:42
# @Author  : iGolden
# @Software: PyCharm
from sqlalchemy import Column, Integer, Float, String, Boolean
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import Base
from flask_login import UserMixin
from app import login_manager


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    _password = Column('password', String(128))
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        pass

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def ckeck_password(self, raw):
        return check_password_hash(self._password, raw)


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
