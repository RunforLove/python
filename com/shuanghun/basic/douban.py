import urllib.request

#网址
url = "http://www.cnblogs.com/runforlove"
#请求
request = urllib.request.Request(url)
#结果
response = urllib.request.urlopen(request)
data = response.read().decode('utf-8')
print(data)
# number = input()
number = 30
if number >= 0:
    number = 100;
else:
    number = -100;
print("Hello world!", number)
str = "i \'m fine, \"thank you\" "
print(str)
print("########################")
print(ord('A'))
print(chr(65))
print(u'sskk')
print("########################")
mylist = ['a','b','c']
print(mylist,len(mylist),mylist[2])
mylist.append('d')
print(mylist[3])
mylist.insert(2,'f')
print(mylist[2])
print("########################")
