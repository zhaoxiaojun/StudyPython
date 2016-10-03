#coding=utf8
import json

#编码
obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
encodedjson = json.dumps(obj)
print encodedjson    #[[1, 2, 3], 123, 123.123, "abc", {"key2": [4, 5, 6], "key1": [1, 2, 3]}]
print type(encodedjson)  #<type 'str'>
print repr(encodedjson)   #'[[1, 2, 3], 123, 123.123, "abc", {"key2": [4, 5, 6], "key1": [1, 2, 3]}]'

#解码
decodejson = json.loads(encodedjson)
print decodejson  #[[1, 2, 3], 123, 123.123, u'abc', {u'key2': [4, 5, 6], u'key1': [1, 2, 3]}]
print type(decodejson)  #<type 'list'>

