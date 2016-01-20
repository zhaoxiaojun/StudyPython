#coding=utf8
import requests

resp = requests.get('http://www.51testing.com/html/index.html')
userdata = {"firstname": "John", "lastname": "Doe", "password": "jdoe123"}
resp = requests.post('http://www.51testing.com/html/index.html', params=userdata)
resp = requests.put('http://www.51testing.com/html/index.html')
resp = requests.delete('http://www.51testing.com/html/index.html')

print resp.json()   # 假如返回的是json数据
print resp.text     #返回的不是text数据
print resp.headers['content-type']  #返回text/html;charset=utf-8

#f = open('request_index.html', 'w')
#f.write(page.encode('utf8'))




