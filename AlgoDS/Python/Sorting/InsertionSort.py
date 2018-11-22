def insertionSort(arr):

    for index in range (1,len(arr)):

        currentValue= arr[index]
        position=index

        while position>0 and arr[position-1]>currentValue:
            arr[position]=arr[position-1]
            position=position-1

        arr[position]=currentValue
    return arr

arr=[3,6,1,12,9]

print('sorted array',insertionSort(arr))