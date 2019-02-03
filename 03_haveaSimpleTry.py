#-*-coding:utf-8-*-
#查找带有href属性的a标签
import requests
from bs4 import BeautifulSoup
import re
res = requests.get('https://news.sina.com.cn/china/')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,features="lxml")

def has_href(tag):
    return tag.has_attr('href') and tag.name == 'a' and len(tag.text)>5 and len(tag.contents)<2 and tag.text.find('\n')==-1 and tag['href'].find('shtml')!=-1

for news in soup.find_all(has_href):
     title = news.text
     ahref = news['href']
     time = re.match(r'.*([0-9]{4}-[0-9]{2}-[0-9]{2})',news['href']).group(1)
     print time,title,ahref