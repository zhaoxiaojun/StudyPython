#coding=utf8


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

if __name__ == '__main__':
    try:
        raise MyError('sdfsdfsdfsdfsd')
    except MyError as e:
        print 'My exception occurred, value:', e.value
