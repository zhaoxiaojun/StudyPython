#coding=utf8
from distutils.core import setup
from distutils.extension import Extension


setup(name='foobar',
    version='1.0',
    ext_modules=[Extension('foo', ['foo.c',])],  #扩展模块由选项ext_modules指定  底层的扩展构建机制是由build_ext命令实现的
    #ext_modules=[Extension('foopkg.foo', ['foo.c'])],
)
'''
生成的文件:
\usr\lib\python2.7\site-packages\foobar-1.0-py2.7.egg-info
\usr\lib\python2.7\site-packages\foo.so

# \usr\lib\python2.7\site-packages\foobar-1.0-py2.7.egg-info
# \usr\lib\python2.7\site-packages\foopkg\foo.so
'''
