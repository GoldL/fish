##### 1.  `python`创建虚拟环境[`pipenv`](https://juejin.im/post/5ca4be8bf265da30b160de27)
```
// 创建虚拟环境
pipenv instal
// 卸载虚拟环境
pipenv --rm
// 进入虚拟环境
pipenv shell
// 虚拟环境下载包
pipenv install flask
// 虚拟环境卸载包
pipenv uninstall flask
// 查看虚拟环境
pipenv --venv
// 推出虚拟环境
exit
// 在Pipfile中的url里切换清华源
https://pypi.tuna.tsinghua.edu.cn/simple/
```
##### 2. [vscode配置Pipenv工作环境](https://shansan.top/2019/03/03/vscode%E9%85%8D%E7%BD%AEPipenv%E5%B7%A5%E4%BD%9C%E7%8E%AF%E5%A2%83/)
1. `pipenv shell`  ---- 先激活Pipenv环境
2. `pipenv --venv` ---- 获取当前虚拟环境的位置
3. `Ctrl+Shift+P`  ---- 输入settings，选择Open Settings(JSon)
```
{
  "python.pythonPath": "/Users/igolden/.local/share/virtualenvs/fish-NTvTY8zR/bin/python",
  "python.venvPath": "/Users/igolden/.local/share/virtualenvs/fish-NTvTY8zR"
}
```
4.  重启vscode，左下角可切换配置环境
##### 3. [Flask路由](https://www.w3cschool.cn/flask/flask_routing.html)
- 装饰器
```
@app.route('/hello')
def hello():
    return 'hello world'
```
- 调用add_url_rule
```
def hello_world():
   return ‘hello world’
app.add_url_rule(‘/’, ‘hello’, hello_world)
```
##### 4. [Flask调试模式](https://www.w3cschool.cn/flask/flask_application.html)

```
app = Flask(__name__)
app.config.from_object('config')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=3003)
```
##### 5. [response](https://www.w3cschool.cn/flask/flask_request_object.html)
```
from flask import Flask, make_response
@app.route('/hello')
def hello():
    headers = {
        'content-type': 'text/plain'
    }
    response = make_response('<html></html>', 200)
    response.headers = headers
    return response
```
##### 6. Blueprint
```
from flask import Blueprint

web = Blueprint('web', __name__)
```
##### 7. [requests](https://requests.readthedocs.io/zh_CN/latest/)
```
import requests
class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
```
##### 8.[wtforms](http://flask123.sinaapp.com/article/32/)
```python
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User

class RegisterForm(EmailForm):
    password = PasswordField(validators=[DataRequired('密码不可以为空，请输入你的密码'), Length(6, 32, message='密码有误')])
    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮箱已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('用户昵称已被注册')
```
##### 9. [flask-sqlalchemy](http://www.pythondoc.com/flask-sqlalchemy/quickstart.html)
```python
# Book Model
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default="未名")
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    isbn = Column(String(15), nullable=True, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))
    
# 注册
db.init_app(app)
with app.app_context():
    db.create_all(app=app)

# 基础类
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    #  不创建表
    __abstract__ = True
    status = Column(SmallInteger, default=1)
    
    def set_attr(self, attr_dic):
    for key, value in attr_dic.items():
        if hasattr(self, key) and key != 'id':
            setattr(self, key, value)
# 使用User表
@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attr(form.data)
        // 创建user表
        db.session.add(user)
        db.session.commit()
        redirect(url_for('web.login'))
        return render_template('auth/register.html', form=form)
```
##### 10. [cymysql](https://pypi.org/project/cymysql/)
##### 11. [进程和线程](https://www.liaoxuefeng.com/wiki/1016959663602400/1017627212385376)
##### 12. `json.dumps`
```
json.dumps(books, default=lambda o: o.__dict__)
```
##### 13. [Flask--修改默认的static文件夹的方法](https://www.cnblogs.com/bayueman/p/6612104.html)
```
app = Flask(__name__, static_folder='', static_url_path='')
```
##### 14.[Jinja2](https://www.w3cschool.cn/yshfid/)
##### 15.[url_for](https://www.cnblogs.com/zxt-cn/p/9171960.html)
##### 16.[filter](https://www.runoob.com/python/python-func-filter.html)
```
    def intro(self):
        intro = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return '/'.join(intro)
```
##### 17.[`flask-login`](https://flask-login.readthedocs.io/en/latest/)
```python
# 注册
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# 在用户model中继承UserMixin
from flask_login import UserMixin
from app import login_manager

class User(UserMixin, Base):

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))

# 使用
from flask_login import login_user
login_user(user, remember=True)

```
##### 18.[`with`](https://blog.csdn.net/lxy210781/article/details/81176687)
```python
with open(r'c:\test.txt', 'r') as f:
    data = f.read()
```
##### 19.[事务](https://www.cnblogs.com/icemonkey/p/10503766.html)
```python
# 事务回滚
try:
    gift = Gift()
    gift.isbn = isbn
    gift.uid = current_user.id
    current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
    db.session.add(gift)
    db.session.commit()
except Exception as e:
    db.session.rollback()
    raise e
```
##### 20.[上下文管理器类和上下文管理器装饰器`contextmanager`](https://blog.csdn.net/weixin_42359464/article/details/80742387)
```python
# 重新事件回滚机制封装
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, SmallInteger
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
```
##### 21.重写`filter_by`
```python
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)
        
        
db = SQLAlchemy(query_class=Query)
```
##### [`namedtuple`](https://www.runoob.com/note/25726)
```
from collections import namedtuple

EachGiftWishCount = namedtuple('EachGiftWishCount', ['count', 'isbn'])
```
22.[`flask-mail`](http://www.pythondoc.com/flask-mail/)
```
from flask_mail import Mail
mail = Mail()
mail.init_app(app)

# 声明方法
from flask import current_app, render_template
from flask_mail import Message

from app import mail


def send_mail(to, subject, template, **kwargs):
    msg = Message(
        '[鱼书]' + ' ' + subject,
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[to])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
# 使用
send_mail(form.email.data, '重置你的密码', 'email/reset_password.html', user=user, token='1123')
```
###### 生成token
```
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id', self.id}).decode('utf-8')
        
@classmethod
    def reset_password(cls, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get(uid)
            user.password = new_password
        return True
```
