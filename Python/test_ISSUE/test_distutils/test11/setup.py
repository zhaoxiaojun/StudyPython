#coding=utf8
#安装package data

'''
有时包中还需要安装其他文件，这些文件与包的实现密切相关，或者是包含文档信息的文本文件等，这些文件就叫做package data。使用setup函数中的
package_data参数可以向packages中添加package data
'''


setup(name='mypkg',
    packages=['mypkg'],
    package_dir={'mypkg': 'src/mypkg'},
    package_data={'mypkg': ['data/*.dat']},
)
'''
package_data参数的值必须是个字典，字典的key就是package name，value是个list，其中包含了需要复制到package中的一系列路径。这些路径都是相对于
包目录而言的（比如package_dir）
'''
