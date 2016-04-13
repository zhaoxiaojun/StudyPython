#coding=utf8
import json

'''
JSON 值可以是：
- 数字number（整数或浮点数）
- 字符串string（在双引号中）
- 逻辑值boolean（true 或 false）
- 数组array（在方括号中）
- 对象object（在花括号中）
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
print '\n----------------'

datad = {'水电费sdsdg中文':'水电费sdsdg中文'}
datazs = json.dumps(datad)
print 'datazs: ',datazs
print 'type of datazs: ', type(datazs)

datazu = datazs.decode('gbk')
print 'datazu: ',datazu
print 'type of datazu: ', type(datazu)
print '\n----------------'

datazu1 = json.loads(datazu)
print 'datazu1: ',datazu1
print 'type of datazu1: ', type(datazu1)

datazu2 = json.dumps(datazu1)
print 'datazu2: ',datazu2
print 'type of datazu2: ', type(datazu2)

datazu3 = datazu2.decode('gbk')
print 'datazu3: ',datazu3
print 'type of datazu3: ', type(datazu3)





