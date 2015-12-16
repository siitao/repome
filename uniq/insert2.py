arr = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
for i in range(1,len(arr)):
    if arr[i] < arr[i-1]:
        temp = arr[i]
        for j in range(i,-1,-1):
            if arr[j] > temp:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                print arr
            else:
                continue
