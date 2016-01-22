#coding=utf8
import requests

#resp = requests.get('http://www.51testing.com/html/index.html')
#userdata = {"firstname": "John", "lastname": "Doe", "password": "jdoe123"}

userdata = '''{"function_code":"600021","mobile_phone":"15366300884"}'''
headers = {"TOKEN":"abcdefghijk", "APPID":10}
url = "http://192.168.18.77:8080/uap/api/ups"
resp = requests.post(url, data=userdata, headers=headers)
#resp = requests.put('http://www.51testing.com/html/index.html')
#resp = requests.delete('http://www.51testing.com/html/index.html')

#print resp.json()   # 假如返回的是json数据
print resp.content.decode('utf-8').encode('gbk')     #返回的不是text数据
#print resp.headers['content-type']  #返回text/html;charset=utf-8

#f = open('request_index.html', 'w')
#f.write(page.encode('utf8'))



testurl = '''http://192.168.18.46:5002/niiwoo-api/niwoportservice.svc/PostEveryOneGuaranteeList?jsonString={"Longitude":"113.74541","Latitude":"23.015399","OrderType":"1","PageIndex":"1","PageSize":"10","StatusId":"0"}'''
testurl1 = '''http://192.168.18.46:5002/niiwoo-api/niwoportservice.svc/PostEveryOneGuaranteeList?'''
testparams = '''{"Longitude":"113.74541","Latitude":"23.015399","OrderType":"1","PageIndex":"1","PageSize":"10","StatusId":"0"}'''
testparams1 = {"jsonString":testparams}

resp = requests.post(testurl1, params=testparams1)

print resp.apparent_encoding
resp.encoding = resp.apparent_encoding
print resp.status_code
print resp.content.decode('utf-8').encode('gbk')

