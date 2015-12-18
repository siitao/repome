#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 抓取某个贴吧固定页数的帖子链接和帖子名称
import re
import urllib2
url_head = "http://tieba.baidu.com" 
# 定义过滤规则
reg = '<a href="(.*)" title="(.*)" target'
try:
    tieba = raw_input("please put the tieba name:")
    times = int(raw_input("please input the page number:"))
    with open('tieba_url.txt','w') as f:
        for i in range(0,times,50):
            url = "http://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%d" %(tieba,i)
            data = urllib2.urlopen(url).read()
            result = re.findall(reg,data)  # 在结果中找出符合规则的内容
            for j,k in result:
		print url_head+j,k
	        f.write(url_head+j+' '+k+'\n')      # 把想要的数据存放在一个文件当中
except:
    print "error!! please check the code.."

