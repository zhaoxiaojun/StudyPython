#coding=utf-8
import doctest

def square(x):
    """Squares x.
    >>> square(2)
    4
    >>> square(-2)
    4
    >>> square(5)
    25
    """
    return x * x

if __name__ == '__main__':
    doctest.testmod()
