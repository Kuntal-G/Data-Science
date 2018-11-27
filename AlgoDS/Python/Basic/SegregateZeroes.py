#Move all zeroes to right of array

def moveZeros(arr):

    count=0
    for i in arr:
        if i>0:
            arr[count]=i
            count+=1

    print(count)
    for i in range(count,len(arr)):
        arr[i]=0

    return arr

arr=[0,6,5,0,5,0,4]
print(arr)
print(moveZeros(arr))


#move zeroes to left

def moveZerosLeft(arr):
    count = len(arr)-1
    for i in range(len(arr)-1,-1,-1):
        if arr[i] > 0:
            arr[count] = arr[i]
            count -= 1

    print(count)
    for i in range(0,count+1):
        arr[i] = 0

    return arr


arr = [0, 6, 5, 0, 5, 0, 4]
print(arr)
print(moveZerosLeft(arr))