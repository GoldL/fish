# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 上午11:41
# @Author  : iGolden
# @Software: PyCharm


from app import create_app

app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=3003)
