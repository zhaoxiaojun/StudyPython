#coding=utf8
import json_tools

print dir(json_tools)

a = {"a":{"aa":{"aaa":333,"aaa2":3332},"b":22}}
b = {"a":{"b":22, "aa":{"aaa2":339, "aaa":333}}}
c = 1
d = 2
e = 'sdfsdf'
f = 'sdfsdf'



print json_tools.diff(a,b)
#print json_tools.diff(c,d)
#print json_tools.diff(e,f)



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
print type(json_tools.loads(data))
