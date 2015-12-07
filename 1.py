#!/usr/bin/env python
#coding=utf-8
number1 = 0
number2 = 0
list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
# 求出第一个大的数字
try:
    for i in list:
        if i > number1:
            number1 = int(i)
	    # 根据最大值算出第二大值
        for j in list:
            if number1 > int(j) > number2:
	        number2 = j
    print "the max number is %d the second number is %d" %(number1,number2)
except:
    print "is error please check."


