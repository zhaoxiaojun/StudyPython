#coding=utf8
from distutils.core import setup

setup (
    name = 'fll',
    version = '1.0',
    author = 'Defias',
    author_email = 'Defias@163.com',
    py_modules = ['fll', 'pkg.mod']  #两个模块，一个在root package中，另一个在pkg包中
)
