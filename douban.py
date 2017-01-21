import urllib.request

#网址
url = "http://www.cnblogs.com/runforlove"
#请求
request = urllib.request.Request(url)
#结果
response = urllib.request.urlopen(request)
data = response.read().decode('utf-8')
print(data)
