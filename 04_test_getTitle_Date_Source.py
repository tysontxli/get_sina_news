#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#上面分别是修改解释器和编译器的编码格式

import requests
from bs4 import BeautifulSoup
from datetime import datetime
res = requests.get("https://news.sina.com.cn/c/2019-01-31/doc-ihrfqzka2777216.shtml")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,features='lxml')

print soup.select('.main-title')[0].contents[0]
dt = soup.select('.date')[0].contents[0]
print datetime.strptime(dt,'%Y年%m月%d日 %H:%M')
print soup.select('.source')[0].contents[0]