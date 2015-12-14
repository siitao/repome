#coding=utf-8
# 从小到大 冒泡算法小到大
number_list = [5,3,423,6,65,213,653,54345,1,-1,-9,-100]

	# 多次循环把最二大值第三大值第四大值...依次放在后面
for j in range(len(number_list) - 1):

	# 把最大值移到最后面
    for i in range(len(number_list) - 1): 

		# 比较相邻的值得大小 A>B 就把A,B两值替换
        if number_list[i] > number_list[i + 1]: 
	    tmp_num = number_list[i + 1]
            number_list[i + 1] = number_list[i]
            number_list[i] = tmp_num
            print "j = %d, i=%d, i+1=%d" %(j+1,i,i+1),number_list
print "the last list %s" %number_list


# 从大到小排序
number_list = [5,3,423,6,65,213,653,54345,1,-1,-9,-100]

        # 多次循环把最二小值第三小值第四小值...依次放在后面
for j in range(len(number_list) - 1):

        # 把最小值移到最后面
    for i in range(len(number_list) - 1):

                # 比较相邻的值得大小 A<B 就把A,B两值替换
        if number_list[i] < number_list[i + 1]:
            tmp_num = number_list[i + 1]
            number_list[i + 1] = number_list[i]
            number_list[i] = tmp_num
            print "j = %d, i=%d, i+1=%d" %(j+1,i,i+1),number_list
print "the last list %s" %number_list

