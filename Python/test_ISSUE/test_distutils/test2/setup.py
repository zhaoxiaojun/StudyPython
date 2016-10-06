#coding=utf8
from distutils.core import setup


setup(name='fee',
    version='1.0',
    packages = ['fee']
)
'''
packages参数是一个列表，其中包含了Distutils需要处理（构建、发布、安装等）的所有包
包名和目录名必须能够相互对应，比如在setup脚本中packages = ['foo']，意味着要在setup脚本所在目录下存在相应的foo目录和foo/__init__.py文件，可
以使用package_dir选项来改变这种默认的对应规则
'''
