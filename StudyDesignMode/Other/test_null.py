#coding=utf8
class Null:
    """A class for implementing Null objects.
    This class ignores all parameters passed when constructing or
    calling instances and traps all attribute and method requests.
    Instances of it always (and reliably) do 'nothing'.
    The code might benefit from implementing some further special
    Python methods depending on the context in which its instances
    are used. Especially when comparing and coercing Null objects
    the respective methods' implementation will depend very much
    on the environment and, hence, these special methods are not
    provided here.
    """

    # Object constructing
    def __init__(self, *args, **kwargs):
        "Ignore parameters."
        return None

    # Object calling
    def __call__(self, *args, **kwargs):
        "Ignore method calls."
        return self

    # Attribute handling
    def __getattr__(self, mname):
        "Ignore attribute requests."
        return self

    def __setattr__(self, name, value):
        "Ignore attribute setting."
        return self

    def __delattr__(self, name):
        "Ignore deleting attributes."
        return self

    # Misc.
    def __repr__(self):
        "Return a string representation."
        return "<Null>"

    def __str__(self):
        "Convert to a string and return it."
        return "Null"


def test():
    "Perform some decent tests, or rather: demos."

    # Constructing and calling
    n = Null()
    n = Null('value')
    n = Null('value', param='value')

    n()
    n('value')
    n('value', param='value')

    # Attribute handling
    n.attr1
    n.attr1.attr2
    n.method1()
    n.method1().method2()
    n.method('value')
    n.method(param='value')
    n.method('value', param='value')
    n.attr1.method1()
    n.method1().attr1

    n.attr1 = 'value'
    n.attr1.attr2 = 'value'

    del n.attr1
    del n.attr1.attr2.attr3

    # Representation and conversion to a string
    assert repr(n) == '<Null>'
    assert str(n) == 'Null'


if __name__ == '__main__':
    test()
