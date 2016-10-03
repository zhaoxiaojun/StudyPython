#coding=utf8
'''
向装饰器本身传递参数
'''

# 装饰器是普通的方法
def my_decorator(func):
    print "I am a ordinary function"
    def wrapper():
        print "I am function returned by the decorator"
        func()
    return wrapper

# 所以你可以不通过@调用它
def lazy_function():
    print "zzzzzzzz"
decorated_function = my_decorator(lazy_function)


# 调用一个函数没有什么特别
@my_decorator
def lazy_function():
    print "zzzzzzzz"

print '\n---------------------\n'


# 声明一个用于创建装饰器的函数
def decorator_maker():
    print "I make decorators! I am executed only once: when you make me create a decorator."

    def my_decorator(func):
        print "I am a decorator! I am executed only when you decorate a function."
        def wrapped():
            print ("I am the wrapper around the decorated function. "
                  "I am called when you call the decorated function. "
                  "As the wrapper, I return the RESULT of the decorated function.")
            return func()
        print "As the decorator, I return the wrapped function."
        return wrapped

    print "As a decorator maker, I return a decorator"
    return my_decorator

# 创建一个装饰器，本质上只是一个函数
new_decorator = decorator_maker()
print '\n---------------------\n'

# 使用装饰器装饰函数
def decorated_function():
    print "I am the decorated function."
decorated_function = new_decorator(decorated_function)
print '\n---------------------\n'

# 调用被装饰函数
decorated_function()
print '\n---------------------\n'


#跳过中间变量，做同样的事情
def decorated_function():
    print "I am the decorated function."
decorated_function = decorator_maker()(decorated_function)
print '\n---------------------\n'
decorated_function()
print '\n---------------------\n'


# 使用装饰器语法
@decorator_maker()
def decorated_function():
    print "I am the decorated function."
decorated_function()
print '\n---------------------\n'


# 向装饰器本身传递参数
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
    print "I make decorators! And I accept arguments:", decorator_arg1, decorator_arg2

    def my_decorator(func):
        # 这里能传递参数的能力，是闭包的特性
        print "I am the decorator. Somehow you passed me arguments:", decorator_arg1, decorator_arg2

        # 不要搞混了装饰器参数和函数参数
        def wrapped(function_arg1, function_arg2) :
            print ("I am the wrapper around the decorated function.n"
                  "I can access all the variablesn"
                  "t- from the decorator: {0} {1}n"
                  "t- from the function call: {2} {3}n"
                  "Then I can pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)
        return wrapped
    return my_decorator

@decorator_maker_with_arguments("Leonard", "Sheldon")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print ("I am the decorated function and only knows about my arguments: {0}"
           " {1}".format(function_arg1, function_arg2))
decorated_function_with_arguments("Rajesh", "Howard")

# 注： 装饰器仅在Python代码导入时被调用一次,之后你不能动态地改变参数.当你使用”import x”,函数已经被装饰，所以你不能改变什么
print '\n---------------------\n'













