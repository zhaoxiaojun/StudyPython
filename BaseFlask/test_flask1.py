#coding=utf8
from flask import Flask
from flask import request
from flask import current_app
from flask import make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return make_response('<h1>Home, %s</h1>' % current_app.name, 202)

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()    # Flask自带的Server在本地端口5000上监听




