#coding=utf8
'''
装饰装饰器的装饰器
'''

def decorator_with_args(decorator_to_enhance):
    """
    这个函数将作为装饰器使用
    它必须装饰另一个函数
    它将允许任何接收任意数量参数的装饰器
    方便你每次查询如何实现
    """

    # 同样的技巧传递参数
    def decorator_maker(*args, **kwargs):

        # 创建一个只接收函数的装饰器
        # 但是这里保存了从创建者传递过来的的参数
        def decorator_wrapper(func):

            # 我们返回原始装饰器的结果
            # 这是一个普通的函数，返回值是另一个函数
            # 陷阱：装饰器必须有这个特殊的签名，否则不会生效
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper

    return decorator_maker


# 你创建这个函数是作为一个装饰器，但是给它附加了一个装饰器
# 别忘了，函数签名是： "decorator(func, *args, **kwargs)"
@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    def wrapper(function_arg1, function_arg2):
        print "Decorated with", args, kwargs
        return func(function_arg1, function_arg2)
    return wrapper

# 然后，使用这个装饰器
@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1, function_arg2):
    print "Hello", function_arg1, function_arg2

decorated_function("Universe and", "everything")
