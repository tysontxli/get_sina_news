import requests
res = requests.get('https://news.sina.com.cn/china/')
res.encoding = 'utf-8'
print res.text