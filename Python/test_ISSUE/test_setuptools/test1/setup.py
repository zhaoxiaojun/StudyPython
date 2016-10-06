#coding=utf8
from setuptools import setup, find_packages

'''
setuptools工具针对Python官方的distutils做了很多针对性的功能增强，比如依赖检查，动态扩展等
'''

setup(
    name = "demo",
    version = "0.1",
    packages = find_packages(),  #find_packages默认在和setup.py同一目录下搜索各个含有__init__.py的包
)


'''
执行python setup.py bdist_egg即可打一个包了
'''
