#coding=utf8
#安装其他文件

'''
通过data_files选项来安装除了上面提到过的文件之外的其他文件，比如配置文件，数据文件等。data_files是个列表，列表中的元素是(directory, files)
'''


setup(name='mypkg',
    data_files=[('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),
                  ('config', ['cfg/data.cfg']),
                  ('/etc/init.d', ['init-script'])]
)
'''
(directory, files)中，directory表示文件最终要被安装到的地方，如果它是相对路径的话，则是相对于installation prefix而言（对于纯python包而言，
就是sys.prefix；对于扩展包，则是sys.exec_prefix）。files是要安装的文件，其中的目录信息（安装前）是相对于setup.py所在目录而言的，安装时，
setup.py根据files的信息找到该文件，然后将其安装到directory中
'''
