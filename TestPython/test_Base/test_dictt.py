#coding=utf8


#用zip反转字典
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print m.items()
print zip(m.values(), m.keys())
mi = dict(zip(m.values(), m.keys()))
print mi



#字典推导
m = {x: x ** 2 for x in range(5)}
print m                            #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
m = {x: 'A' + str(x) for x in range(10)}
print m                            #{0: 'A0', 1: 'A1', 2: 'A2', 3: 'A3', 4: 'A4', 5: 'A5', 6: 'A6', 7: 'A7', 8: 'A8', 9: 'A9'}


#用字典推导反转字典
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print m
print {v: k for k, v in m.items()}
