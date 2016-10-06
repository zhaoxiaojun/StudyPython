#coding=utf8
from distutils.core import setup


setup(name='fee',
    version='2.0',
    package_dir = {'':'lib'},
    packages = ['fee']
)
'''
package_dir是个字典，其中的key是要安装的包名，如果为空，则表明是root package，value就是该包（key）对应的源码树的目录
'''
