# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 下午5:46
# @Author  : iGolden
# @Software: PyCharm
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
