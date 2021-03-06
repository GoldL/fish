# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 上午12:04
# @Author  : iGolden
# @Software: PyCharm
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo

from app.models.user import User


class EmailForm(Form):
    email = StringField(
        validators=[DataRequired(), Length(8, 64, message='邮箱地址在长度8-64字符之间')])


class RegisterForm(EmailForm):
    password = PasswordField(validators=[DataRequired('密码不可以为空，请输入你的密码'), Length(6, 32, message='密码有误')])
    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮箱已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('用户昵称已被注册')


class LoginForm(EmailForm):
    password = PasswordField(validators=[DataRequired('密码不可以为空，请输入你的密码'), Length(6, 32)])


class ResetPasswordForm(Form):
    password1 = PasswordField('新密码', validators=[
        DataRequired(), Length(6, 20, message='密码长度至少需要在6到20个字符之间'),
        EqualTo('password2', message='两次输入的密码不相同')])
    password2 = PasswordField('确认新密码', validators=[
        DataRequired(), Length(6, 20)])
