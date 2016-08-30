#coding=utf8
from tornado.template import Template

print Template("{{ 1+1 }}").generate()

print Template("{{ 'scrambled eggs'[-4:] }}").generate()

print Template("{{ ', '.join([str(x*x) for x in range(10)]) }}").generate()

print Template("{{roads}}").generate(roads='hellosss')

def disemvowel(s):
    return ''.join([x for x in s if x not in 'aeiou'])

print disemvowel("george")

#模板中使用自己编写的函数
print Template("my name is {{d('mortimer')}}").generate(d=disemvowel)


"""
模板语法提要：
1、在双大括号（{{和}}）中的单词是占位符，当我们渲染模板时希望以实际值代替，可以将任何Python表达式放在双大括号中
2、支持if、for、while和try。在这些情况下，语句块以{%开始，并以%}结束
3、模板中默认提供的函数：
    escape(s)
    替换字符串s中的&、<、>为他们对应的HTML字符。

    url_escape(s)
    使用urllib.quote_plus替换字符串s中的字符为URL编码形式。

    json_encode(val)
    将val编码成JSON格式。（在系统底层，这是一个对json库的dumps函数的调用。查阅相关的文档以获得更多关于该函数接收和返回参数的信息。）

    squeeze(s)
    过滤字符串s，把连续的多个空白字符替换成一个空格
4、在Tornado 1.x中，模版不是被自动转义的。在Tornado 2.0中，模板被默认为自动转义（可以在Application构造函数中使用autoscaping=None关闭或在模板文件中使用 {% autoescape None %} 语句）
5、模板中可以使用一个自己编写的函数
"""
