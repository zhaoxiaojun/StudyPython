#coding=utf8
'''
工厂模式是一种创建型的设计模式，作用如其名称：这是一个就像工厂那样生产对象实例的类
这个模式的主要目的是将可能涉及到很多类的对象创建过程封装到一个单独的方法中。通过给定的上下文输出指定的对象实例
'''

class Button(object):
    html = ""
    def get_html(self):
        return self.html

class Image(Button):
    html = "<img alt=\"\" />"

class Input(Button):
    html = "<input type=\"text\" />"

class Flash(Button):
    html = "flash"

class ButtonFactory():
    def create_button(self, typ):
        targetclass = typ.capitalize()
        return globals()[targetclass]()
'''
globals()将以字典的方式返回所有全局变量，因此targetclass = typ.capitalize()将通过传入的typ字符串得到类名(Image、Input或Flash)，而globals()[targetclass]将通过类名
取到类的类(见元类)，而globals()[targetclass]()将创建此类的对象。
'''

button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
    print button_obj.create_button(b).get_html()
