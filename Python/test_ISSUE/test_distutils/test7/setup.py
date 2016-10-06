#coding=utf8
from distutils.core import setup


setup(name='foobar',
    version='1.0',
    package_dir={'': 'src'},  #这种情况依然可以用声明root包的方式来发布，只不过需要使用package_dir选项来指明包和目录的关系
    packages=[''],
)
