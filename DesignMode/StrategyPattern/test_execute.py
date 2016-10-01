#coding=utf8
import types

class StrategyExample:
    def __init__(self, func=None):
        self.name = 'Strategy Example 0'
        if func is not None:
            self.execute = types.MethodType(func, self)  #动态绑定func到实例上的execute， 原来的execute被覆盖

    def execute(self):
        print(self.name)

def execute_replacement1(self):
    print(self.name + ' from execute 1')


def execute_replacement2(self):
    print(self.name + ' from execute 2')


if __name__ == '__main__':
    strat0 = StrategyExample()
    strat0.execute()

    strat1 = StrategyExample(execute_replacement1)
    strat1.execute()
    strat1.name = '1111111111'
    strat1.execute()



