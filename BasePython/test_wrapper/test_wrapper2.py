#coding=utf8
'''
理解装饰器
'''

# 装饰器是一个以另一个函数为参数的函数
def my_shiny_new_decorator(a_function_to_decorate):

    # 在这里，装饰器定义一个函数： 包装器.
    # 这个函数将原始函数进行包装，以达到在原始函数之前、之后执行代码的目的
    def the_wrapper_around_the_original_function():

        # 将你要在原始函数之前执行的代码放到这里
        print "Before the function runs"

        # 调用原始函数(需要带括号)
        a_function_to_decorate()

        # 将你要在原始函数之后执行的代码放到这里
        print "After the function runs"

    # 代码到这里，函数‘a_function_to_decorate’还没有被执行
    # 我们将返回刚才创建的这个包装函数
    # 这个函数包含原始函数及要执行的附加代码，并且可以被使用
    return the_wrapper_around_the_original_function

# 创建一个函数
def a_stand_alone_function():
    print "I am a stand alone function, don't you dare modify me"

a_stand_alone_function()
print '\n---------------------\n'

# 好了，在这里你可以装饰这个函数，扩展其行为
# 将函数传递给装饰器，装饰器将动态地将其包装在任何你想执行的代码中，然后返回一个新的函数
a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
# 或： a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)  #让返回的新函数与被装饰的原函数同名

# 调用新函数，可以看到装饰器的效果
a_stand_alone_function_decorated()
#或：a_stand_alone_function()  # 这就是装饰器做的事情!
print '\n---------------------\n'

# 使用装饰器语法
# 装饰器只是装饰器模式的python实现
@my_shiny_new_decorator
def another_stand_alone_function():
    print "Leave me alone"

another_stand_alone_function()
print '\n---------------------\n'



#累加装饰器
def bread(func):
    def wrapper():
        print "/''''''>"
        func()
        print "______/>"
    return wrapper

def ingredients(func):
    def wrapper():
        print 11111111
        func()
        print 22222222
    return wrapper

def sandwich(food="--ham--"):
    print food

sandwich()
print '\n---------------------\n'

#累加两个装饰器
sandwich = bread(ingredients(sandwich))
sandwich()
print '\n---------------------\n'


# 使用装饰器语法
# 装饰器位置的顺序很重要
@bread
@ingredients
def sandwich(food="--ham--"):
    print food
sandwich()
print '\n---------------------\n'


# 向装饰器函数传递参数
# 这不是黑魔法，你只需要让包装传递参数:
def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):  # 当你调用装饰器返回的函数，实际上是调用包装函数，所以给包装函数传递参数即可将参数传给装饰器函数
            print "I got args! Look:", arg1, arg2
            function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments


@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print "My name is", first_name, last_name

print_full_name("Peter", "Venkman")
print '\n---------------------\n'



# 装饰方法
# Python中对象的方法和函数是一样的，除了对象的方法首个参数是指向当前对象的引用(self)。这意味着你可以用同样的方法构建一个装饰器，只是必须考虑self
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3 # very friendly, decrease age even more :-)
        return method_to_decorate(self, lie)
    return wrapper

class Lucy(object):
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print "I am %s, what did you think?" % (self.age + lie)

l = Lucy()
l.sayYourAge(-3)
print '\n---------------------\n'



#通用的装饰器
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # 包装函数可以接受任何参数
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print "Do I have args?:"
        print args
        print kwargs
        # 然后你可以解开参数， *args，**kwargs
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print "Python is cool, no argument here."
function_with_no_argument()

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print a, b, c
function_with_arguments(1,2,3)


@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Why not ?"):
    print "Do %s, %s and %s like platypus? %s" %
    (a, b, c, platypus)
function_with_named_arguments("Bill", "Linus", "Steve", platypus="Indeed!")


class Mary(object):
    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3): # You can now add a default value
        print "I am %s, what did you think ?" % (self.age + lie)

m = Mary()
m.sayYourAge()
