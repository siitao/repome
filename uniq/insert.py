arry=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
n = len(arry)    
for i in range(n):
    for j in range(1,n-i):
        if  arry[j-1] > arry[j]:
            arry[j-1],arry[j] = arry[j],arry[j-1]     
            print arry
