#coding=utf8
#配置文件


'''
在构建发布时无法将所有的选项都确定下来，有些选项的值可能来自于用户，或者用户的系统。这也就是配置文件setup.cfg存在的目的，用户可以通过修改该配
置文件进行选项的配置

在构建时，选项的处理顺序是setup脚本、配置文件，命令行。所以，安装者可以通过修改setup.cfg文件来覆盖setup.py中的选项；也可以通过运行setup.py时
的命令行选项，来覆盖setup.cfg

配置文件的基本语法如下：
[command]
option=value

command就是Distutils的命令（比如build_py，install等），option就是命令支持的选项。配置文件中的空行、注释（以’#’开头，直到行尾）会被忽略

可以通过--help选项得到某个命令支持的选项，比如：python setup.py --help build_ext

'''
