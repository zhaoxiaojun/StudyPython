#cdoing=utf8

def is_odd(n):
    return n % 2 == 1

a = [1, 2, 4, 5, 6, 9, 10, 15]
a = filter(is_odd, a)
print a
