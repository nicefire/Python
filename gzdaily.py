#!/usr/bin/python
#coding=utf-8

#Programe Name:
#Version:
#用来下载广州日报文字的
#Author:
#QQ:
#E-mail:

import urllib2,re,sys

#url = sys.argv[1]

url = "http://gzdaily.dayoo.com/html/2013-02/05/content_2147118.htm"

content = urllib2.urlopen(url).read()
#print content

title = re.search(r'<h3 id="artTitle">.*</h3>',content)
new = re.search(r'<founder-content>.*</founder-content>',content,re.M|re.S)

title = title.group()
text = new.group()
def html_to_text(text):
    text = text.replace("<P>","\n")
    text = text.replace("</P>","")
    text = text.replace("&nbsp;"," ")
    text = text.replace("<founder-content>","")
    text = text.replace("</founder-content>","")
    return text

def title_to_text(text):
    text = text.replace('<h3 id="artTitle">',"")
    text = text.replace("</h3>","")
    return text

print title_to_text(title)
print html_to_text(text)

f = open(title_to_text(title).decode('utf-8').encode('gbk')+".txt","w")
f.write(title_to_text(title))
f.write(html_to_text(text))
f.close()