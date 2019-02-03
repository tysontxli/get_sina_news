#-*-coding:utf-8-*-
import re
import json
import requests

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

newsurl = "https://news.sina.com.cn/c/2019-01-31/doc-ihrfqzka2777216.shtml"

print getCommentCounts(newsurl)