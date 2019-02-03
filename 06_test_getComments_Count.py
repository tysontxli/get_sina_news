#-*-coding:utf-8
import requests
import json

#仔细看新闻id，并且去掉一些参数
res1 = requests.get('https://comment.sina.com.cn/page/info?versi\
on=1&format=json&channel=gn&newsid=comos-hrfqzka2777216&group=u\
ndefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=\
3&h_size=3')

commentjson = json.loads(res1.text)
print commentjson
print commentjson['result']['count']['total']