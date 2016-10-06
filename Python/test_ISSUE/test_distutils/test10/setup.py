#coding=utf8
from distutils.core import setup
from distutils.extension import Extension

#扩展包

setup(name = 'foobar',
    version = '1.0',
    ext_package = 'pkg',  #如果一个包下有多个扩展，而且要把这些扩展都放在统一的目录下，则可以使用ext_package关键字
    ext_modules = [Extension('foo', ['src/foo.c']),
                    Extension('subpkg.bar', ['src/bar.c'])
    ]
)
'''
将会编译src/foo.c为pkg.foo，将src/bar.c编译为pkg.subpkg.bar

Extension构建函数的第二个参数是源文件的列表，目前Distutils仅支持C、C++和Objective-C扩展，还可以在列表中包含SWIG接口文件（.i文件）
setup(...,
      ext_modules=[Extension('_foo', ['foo.i'],
                             swig_opts=['-modern', '-I../include'])],
      py_modules=['foo'],
)

Extension还可以指定其他选项，比如可以指定头文件目录，define或undefine宏、需要链接的库，链接时和运行时搜索库的路径等等
'''
