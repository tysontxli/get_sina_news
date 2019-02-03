#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#上面分别是修改解释器和编译器的编码格式
import re
import json
import requests
from bs4 import BeautifulSoup

def getCommentCounts(newsurl):
    """
    根据newsurl来获取newsid
    :param newsurl:
    :return:newsid
    """
    requestURL = "https://comment.sina.com.cn/page/info?version=1&format=json&\
channel=gn&newsid=comos-{}&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1\
&page_size=3&t_size=3&h_size=3" #注意这里传递参数的方法
    getCountRequestUrl = requestURL.format(re.search('doc-i(.+).shtml',newsurl).group(1))
    commentes = requests.get(getCountRequestUrl)
    jd = json.loads(commentes.text)
    return jd['result']['count']['total']

def getNewsDetail(newsurl):
    res = requests.get(newsurl)
    result = {}
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.content, features='lxml')
    result['title'] = soup.select('.main-title')[0].contents[0]
    dt = soup.select('.date')[0].contents[0]
    # result['dt'] =datetime.strptime(dt, '%Y年%m月%d日 %H:%M')
    result['newssource'] =soup.select('.source')[0].contents[0]
    result['article'] = ' '.join(p.text.encode('utf-8').decode('utf-8').strip() for p in soup.select('#article p')[:-1])
    result['editor'] =soup.select('.show_author')[0].text.lstrip('责任编辑：')
    result['commentsCount'] = getCommentCounts(newsurl)
    return json.dumps(result, encoding="UTF-8", ensure_ascii=False)

print getNewsDetail("https://news.sina.com.cn/c/2019-01-31/doc-ihrfqzka2777216.shtml")