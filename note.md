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
```
from wtforms import Form, StringField
from wtforms.validators import Length
class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30)])
```
##### 9. [flask-sqlalchemy](http://www.pythondoc.com/flask-sqlalchemy/quickstart.html)
```
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
db.create_all(app=app)
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
##### 14[Jinja2](https://www.w3cschool.cn/yshfid/)
##### 15[url_for](https://www.cnblogs.com/zxt-cn/p/9171960.html)
##### 16[filter](https://www.runoob.com/python/python-func-filter.html)
```
    def intro(self):
        intro = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return '/'.join(intro)
```