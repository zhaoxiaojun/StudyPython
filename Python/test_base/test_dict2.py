#coding=utf8


seq = {'name', 'age', 'sex'}

dsq = dict.fromkeys(seq)  #dict.fromkeys(seq[, value])) 创建一个新的字典，键为seq序列中提供的值，每个键的值都为提供的value，不提供时为None
print dsq

dsq = dict.fromkeys(seq, 10)
print dsq


dsw = dict(name='Bob', age=42)
print dsw
