#coding=utf-8
import pytest


#用于判断素数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


# 判断是否为素数
def test_true():
    assert is_prime(13)


# 判断是否不为素数
def test_true():
    assert not is_prime(7)

if __name__ == '__main__':
    pytest.main("test_assert3.py")
