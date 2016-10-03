#coding=utf8
import pyperclip

#跨平台的对系统剪贴板操作的方法

pyperclip.copy("docs.python.org")

dd = pyperclip.paste()

print(dd)

