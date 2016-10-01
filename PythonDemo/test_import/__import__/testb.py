#encoding: utf-8

"""
同import语句同样的功能，但__import__是一个函数，并且只接收字符串作为参数。其实import语句就是调用这个函数进行导入工作的，
import sys <==>sys = __import__('sys')
"""

import sys
__import__('testa')      #第一次导入会打印消息
del sys.modules['testa']   #unimport
__import__('testa')    #再次导入还是会打印消息，因为已经unimport一次了
__import__('testa')    #这次就不会打印消息了


"""
__import__()的完全调用形式是 __import__(name, globals, locals, fromlist),name 即模块名、其后是全局和局部变量，最后是在模块中要导入的列表。比如：
__import__('string', globals(), locals(), ['join', 'split'])

通常在动态加载时可以使用到这个函数，比如你希望加载某个文件夹下的所用模块，但是其下的模块名称又会经常变化时，就可以使用这个函数动态加载所
有模块了，最常见的场景就是插件功能的支持
"""
