# Binary search implementation O(logN)
def binarySearch(arr,k):

    low=0
    high=len(arr)-1
    found= False

    while low<=high and not found:
        mid = (low + high) // 2

        if k == arr[mid]:
            found=True
            print('Element {} found at position {}'.format(k,mid))

        else:
            if k>arr[mid]:
                low=mid +1
            else:
                high=mid-1
    return found

arr=[2,4,6,8.10]
print(binarySearch(arr,6))





