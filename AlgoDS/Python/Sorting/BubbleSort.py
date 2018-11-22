def bubbleSort(arr):

    for passnum in range(len(arr)-1,0,-1):

        for i in range(passnum):

            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                # or instead of temp variable use python variable swap
                # arr[i],arr[i+1]=arr[i+1],arr[i]

    return arr

arr=[2,8,5,13,1]

print('Initial array',arr)
print('Sorted array', bubbleSort(arr))