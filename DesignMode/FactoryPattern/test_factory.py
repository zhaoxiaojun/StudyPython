#coding=utf8
'''
工厂模式
定义：定义一个用于创建对象的接口，让子类决定实例化哪一个类，工厂方法使一个类的实例化延迟到其子类
类型：创建类模式
'''
class Button(object): #父类
    html = ""
    def get_html(self):
        return self.html

class Image(Button):  #子类
    html = "<img alt=\"\" />"

class Input(Button):  #子类
    html = "<input type=\"text\" />"

class Flash(Button):  #子类
    html = "flash"

class ButtonFactory(): #工厂
    def create_button(self, typ):
        targetclass = typ
        return globals()[targetclass]()
'''
globals()将以字典的方式返回所有全局变量，因此targetclass = typ.capitalize()将通过传入的typ字符串得到类名(Image、Input或Flash)，而globals()[targetclass]将通过类名
取到类的类(见元类)，而globals()[targetclass]()将创建此类的对象。
'''

button_obj = ButtonFactory()
button = ['Image', 'Input', 'Flash'] #子类名的字符串
for b in button:
    print button_obj.create_button(b).get_html()
