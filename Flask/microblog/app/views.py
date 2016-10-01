#coding=utf8
from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel123' }
    return render_template("index.html",   #render_template函数需要传入模板名以及一些模板变量列表，返回一个所有变量被替换的渲染的模板
                                           #在内部render_template调用了Jinja2模板引擎，Jinja2模板引擎是Flask框架的一部分。Jinja2会把模板参数提供的相应的值替换了{{...}}块
        #title = 'Home',
        user = user)
