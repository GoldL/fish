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