#!usr/bin/env python
#coding=utf-8
arr=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
lists=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
print arr
for j in range(1,len(arr)):
    if arr[j-1] > arr[j]:
	arr[j-1],arr[j] = arr[j],arr[j-1]
	print arr

print "--------------------------------------------"

print lists
for i in range(1, len(lists)):
    key = lists[i]
    j = i - 1
    while j >= 0:
        if lists[j] > key:
            lists[j + 1] = lists[j]
            lists[j] = key
        j -= 1
    print lists
