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
soup = BeautifulSoup(res.content,features='lxml')

article= []

print ' '.join(p.text.encode('utf-8').decode('utf-8').strip() for p in soup.select('#article p')[:-1])
print soup.select('.show_author')[0].text.lstrip('责任编辑：')
