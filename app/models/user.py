# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 下午11:42
# @Author  : iGolden
# @Software: PyCharm
from sqlalchemy import Column, Integer, Float, String, Boolean

from app.models.base import Base


class User(Base):
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
