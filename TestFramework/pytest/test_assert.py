#coding=utf-8
import pytest

#pytest测试框架中并没提供特殊的断言方法，而是直接使用python的assert进行断言


# 功能
def add(a,b):
    return a + b

# 测试相等
def test_add():
    assert add(3,4) == 7

# 测试不相等
def test_add2():
    assert add(17,22) != 50

# 测试大于
def test_add3():
    assert add(17,22) <= 50

# 测试小于
def test_add4():
    assert add(17,22) >= 50


if __name__ == '__main__':
    pytest.main("test_assert.py")
