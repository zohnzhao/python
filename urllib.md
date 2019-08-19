import urllib.request

# 简单的 get
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))

print('-' * 40)

# 简单的传递参数
import urllib.parse

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))
print('-' * 40)

# 超时时间
response = urllib.request.urlopen('http://www.baidu.com', timeout=1)
print(response.read().decode('utf-8'))

print('-' * 40)

# 响应类型
print(type(response))
print('-' * 40)

# 状态码，响应头
response = urllib.request.urlopen('https://www.python.org')
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
print('-' * 40)

# Request 对象
request = urllib.request.Request('https://www.python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
print('-' * 40)

# header 与 post
from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'Host': 'httpbin.org',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
dicts = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dicts), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
print('-' * 40)

# 额外添加header
url = 'http://httpbin.org/post'
headers = {
    'Host': 'httpbin.org',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
dicts = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dicts), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
req.add_header('Accept-Encoding', 'gzip, deflate, br')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
print('-' * 40)

# Handler 代理

proxy_handler = urllib.request.ProxyHandler(
    {
        'http': 'http://127.0.0.1:9743',
        'https': 'http://127.0.0.1:9743'
    }
)
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
print('-' * 40)

# Cookie
import http.cookiejar

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)

# 忽略证书
import ssl

context = ssl._create_unverified_context()
response = urllib.request.urlopen(req, context=context)
