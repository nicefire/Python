#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
程序名：每日获取51cto下载豆,家园签到
日  期：2012-12-18
版  本：1.0
'''
import urllib2,cookielib,urllib,re,random

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

def login(username):
	#登陆，获取token，PHPSESSID
	url = 'http://home.51cto.com/index.php?s=/Index/doLogin'
	postDict = {
				'email':username,
				'passwd':'这里是你的密码',
				'autologin':'on',
				'reback':'http://down.51cto.com',
				'button.x':'18',
				'button.y':'7',
			}
	postData = urllib.urlencode(postDict)
	req = urllib2.Request(url, postData)
	req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0");
	req.add_header('Content-Type', "application/x-www-form-urlencoded");
	resp = urllib2.urlopen(req)
	con = urllib2.urlopen(req).read()
	content = re.findall(r'http.*?"',con,re.M|re.S)
	resp = urllib2.urlopen(content[1])

def getfreecredits(username):
	url = 'http://down.51cto.com/download.php?do=getfreecredits&t='+str(random.random())
	req = urllib2.Request(url)
	req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0")
	req.add_header('Content-Type', "application/x-www-form-urlencoded")
	resp = urllib2.urlopen(req).read()
	if int(resp)==1:
		print username.decode("utf-8").encode("gbk"),"您今天已经领取过了下载豆".decode("utf-8").encode("gbk")
	elif int(resp)==0:
		print username.decode("utf-8").encode("gbk"),"领取失败！".decode("utf-8").encode("gbk")
	else:
		print "当前账户".decode("utf-8").encode("gbk"),username.decode("utf-8").encode("gbk"),"已经有下载豆：".decode("utf-8").encode("gbk"),resp,'颗！'.decode("utf-8").encode("gbk")

def toSign():
	url = 'http://home.51cto.com/index.php?s=/Home/toSign'
	req = urllib2.Request(url)
	req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0");
	req.add_header('Content-Type', "application/x-www-form-urlencoded");
	resp = urllib2.urlopen(req).read()
	print resp

#请修改自己的用户米
usernames = ('这里是用户名')

for username in usernames:
	login(username)
	getfreecredits(username)
	toSign()
	cj.clear()

