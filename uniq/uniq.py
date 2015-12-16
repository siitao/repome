#!/usr/bin/env python
#ecoding=utf-8
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,-1,-9,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14,-1,-9]
arr3 = []
arr4 = []

for i in arr2:
    if i in arr1:
        arr3.append(i)
	print arr3
	print "-------"
	for j in range(len(arr3)-1):
            if arr3[j] > arr3[j+1]:
	        arr3[j],arr3[j+1] = arr3[j+1],arr3[j]
                arr4.append(arr3[j])
print arr4
