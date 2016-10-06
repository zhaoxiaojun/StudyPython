#coding=utf8
from distutils.core import setup


setup(name = "foo",  #包名
    version = "1.0.0",   #版本号
    description = "Distutils Sample distribution foo",   #描述信息
    author='Defias',
    author_email='defias@xxx.com',
    url='https://github.com/gdefias',
    py_modules = ['foo'],   #发布的模块列表
)

'''
setup脚本：
是使用Distutils构建、发布和安装模块的核心。setup脚本的作用是向Distutils描述发布模块的信息
主要是调用setup函数，而且模块开发者向Distutils提供的模块信息多数是由setup函数的关键字参数提供的
'''

'''
编写好setup.py之后，就可以创建该模块的源码发布了：
python setup.py sdist
#python setup.py sdist --owner=root --group=root  #指定用户和群组

sdist命令会创建一个archive文件（置于dist目录中，比如Unix上的tar文件，Windows上的zip文件等），它包含setup.py， foo.py。该archive文件命名为
foo-1.00.tar.gz(zip)，解压之后的目录名是foo-1.0。如果一个用户希望安装foo模块，他只需要下载foo-1.0.tar.gz，解压，进入foo-1.0目录，然后运行：
python setup.py install
（运行install命令，会首先运行build命令，然后运行子命令install_lib,install_data和install_scripts）

该命令最终会将foo.py复制到Python环境存放第三方模块的目录中，该命令生成的文件是：
/usr/lib/python2.7/site-packages/foo-1.0-py2.7.egg-info
/usr/lib/python2.7/site-packages/foo.py
/usr/lib/python2.7/site-packages/foo.pyc

其他构建发布命令：
#在Windows中，可以使用bdist_wininst命令创建一个exe安装文件
python setup.py bdist_wininst

#创建RPM文件
python setup.py bdist_rpm

#Solaris pkgtool
python setup.py bdist_pkgtool

#HP-UX swinstall
python setup.py  bdist_sdux

发布和包有三种关系：它依赖其他包，它服务于其他包，它淘汰其他包。这些关系可以分别用setup函数的参数requires，provides和obsoletes来指定
'''

