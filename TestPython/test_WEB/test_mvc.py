#coding=utf8
from flask import Flask, request, render_template

'''
MVC：Model-View-Controller，中文名“模型-视图-控制器”。
Python处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等
包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML
M：Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据
Python支持关键字参数，很多Web框架允许传入关键字参数，然后，在框架内部组装出一个dict作为Model（如:{ 'name': 'Michael' }）
'''

'''
模板技术：
使用模板，需要预先准备一个HTML文档，这个HTML文档不是普通的HTML，而是嵌入了一些变量和指令，然后，根据我们传入的数据，替换后，得到最终的HTML，发送给用户

'''

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')   #通过render_template()函数来实现模板的渲染。和Web框架类似，Python的模板也有很多种。Flask默认支持的模板是jinja2

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username, password=password)
    return render_template('form.html', message='Bad username or password', username=username)

#有了MVC，我们就分离了Python代码和HTML代码。HTML代码全部放到模板里，写起来更有效率


if __name__ == '__main__':
    app.run()


'''
除了Jinja2，常见的模板还有：
Mako：用<% ... %>和${xxx}的一个模板；
Cheetah：也是用<% ... %>和${xxx}的一个模板；
Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。
'''
