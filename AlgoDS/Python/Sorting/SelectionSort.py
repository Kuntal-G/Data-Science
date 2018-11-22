def selectionSort(arr):

    for passnum in range(len(arr)-1,0,-1):

        posMax=0

        for i in range(1,passnum+1):

            if arr[i]>arr[posMax]:
                posMax=i

        arr[passnum],arr[posMax]= arr[posMax],arr[passnum]

    return arr

arr=[3,6,1,12,9]

print('sorted array',selectionSort(arr))