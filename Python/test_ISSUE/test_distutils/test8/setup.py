#coding=utf8
from distutils.core import setup

setup(name='foobar',
    version='1.0',
    package_dir = {'foobar':'src'},
    packages=['foobar', 'foobar.subfoo'],  #如果涉及到子包的话，则必须在packages选项中明确的指出
    #packages=['foobar'],
)
