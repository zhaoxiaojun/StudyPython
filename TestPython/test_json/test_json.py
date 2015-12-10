#coding=utf8
import json

'''
JSON 值可以是：
- 数字（整数或浮点数）
- 字符串（在双引号中）
- 逻辑值（true 或 false）
- 数组（在方括号中）
- 对象（在花括号中）
- null

json.dumps()方法返回了一个str对象encodedjson
json.loads()方法返回了原始的对象，但是仍然发生了一些数据类型的转化。比如，‘abc’转化为了unicode类型
'''

data = '''{
    "userbasicinfo": [
        {
            "LoginFromOthers": "weixin",
            "istuandai": null,
            "name": 123,
            "bbb": true
        },
        {
            "LoginFromOthers": "qq",
            "kong": null,
            "shu": 123,
            "fff": true
        }
    ]
}'''

dataDict = json.loads(data)   #json字符串 --> python对象
print 'dataDict: ', dataDict

data = json.dumps(dataDict)    #python对象 -->  json字符串
print 'data: ', data
