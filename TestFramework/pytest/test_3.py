#coding=utf-8
import pytest
#从Python代码中调用pytest


def test_main():
    assert 5 != 5

if __name__ == '__main__':
    #pytest.main()  #main()默认执行了当前文件所在的目录下的所有测试文件

    pytest.main("-q test_3.py")   #指定测试文件

    #pytest.main(".")  #也可指定测试目录
