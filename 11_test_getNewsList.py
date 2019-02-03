import requests
import json
res = requests.get("https://feed.sina.com.cn/api/roll/get?pageid=121&lid=1356&num=20&versionNumber=1.2.4&page=1&encode=utf-8&callback=feedCardJsonpCallback&_=1549161462841")
res.encoding='utf-8'
print json.loads('{'+res.text.lstrip('try{feedCardJsonpCallback(').rstrip(');}catch(e){};')+'}}')