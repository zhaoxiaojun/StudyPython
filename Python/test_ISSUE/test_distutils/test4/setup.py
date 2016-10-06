#coding=utf8
from distutils.core import setup


setup(name='fee',
    version='2.0',
    package_dir = {'fee':'lib'},
    packages = ['fee', 'fee.bar']
)
'''
fee包对应lib目录，所以，fee.bar包就对应着lib/bar子目录
'''
