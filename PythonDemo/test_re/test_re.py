#coding=utf8
import re

param = '207155115151'
pattern = re.compile(r'^(207|209)\w+')  #匹配userid
match = pattern.match(param)

print match
print bool(match)
print type(match)

if match:
    count = 0
else:
    count = 1
print count
