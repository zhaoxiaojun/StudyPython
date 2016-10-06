#coding=utf8
from distutils.core import setup


setup(name='foobar',
    version='1.0',
    packages=[''],  #即使模块没有放到包中，也可以通过向setup脚本声明root包的方法来发布
)
