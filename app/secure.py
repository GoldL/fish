# @Time    : 2020/4/2 下午3:01
# @Author  : iGolden
# @Software: PyCharm


DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@localhost:3306/fisher'

SECRET_KEY = "iGolden1515"

# email配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '1525922633@qq.com'
# QQ邮箱->设置->账户->[POP3...]->生成授权码->发送短信->获取授权码
MAIL_PASSWORD = 'qilyzdehgrangdaj'
