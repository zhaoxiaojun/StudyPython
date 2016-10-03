#coding=utf8
import sys

print sys.path
print len(sys.path)

'''
sys.path的初始值会受到PYTHONPATH、PYTHONHOME等环境变量的影响
也可以在脚本运行过程中动态修改sys.path从而import自己需要的模块
'''

#添加自己的模块路径
#sys.path.append("mine module path")
#sys.path.insert(0, "mine module path")
#sys.path = []  #删除path中所有路径


#Python解释器中所有内建模块的名称
print sys.builtin_module_names
