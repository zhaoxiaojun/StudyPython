#encoding: utf-8

import testa   #第一次import会打印a里面的语句
print id(testa) #原来a的内存地址
reload(testa)  #第二次reload还会打印a里面的语句，因为有重新加载
print id(testa) #reload后a的内存地址，和原来一样


#对已经加载的模块进行重新加载，一般用于原模块有变化等特殊情况，reload前该模块必须已经import过
#reload会重新加载已加载的模块，但原来已经使用的实例还是会使用旧的模块，而新生产的实例会使用新的模块；reload后还是用原来的内存地址；不能支持from。。import。。格式的模块进行重新加载。
