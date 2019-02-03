#-*-coding:utf-8-*-
import re
#使用字符串切片
newsurl = "https://news.sina.com.cn/c/2019-01-31/doc-ihrfqzka2777216.shtml"
newsid =newsurl.split('/')[-1].rstrip('.shtml').lstrip('doc-i')
print newsid

#或者用正则表达式
#group(0)是引用匹配到的字符串全文，group(1)是引用第一个分组内的部分
print re.search('doc-i(.+).shtml',newsurl).group(0)
print re.search('doc-i(.+).shtml',newsurl).group(1)