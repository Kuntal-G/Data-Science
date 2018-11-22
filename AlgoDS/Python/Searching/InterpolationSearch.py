#Interpolation Search
def interpolationSearch(arr,k):

    low=0
    high=len(arr)-1

    while low<=high and k>=arr[low] and k <=arr[high] :
        pos = low + int(((float(high - low) /(arr[high] - arr[low])) * (k - arr[low])))

        if k == arr[pos]:

            print('Element {} found at position {}'.format(k,pos))
            return pos

        else:
            if k>arr[pos]:
                low=pos+1
            else:
                high=pos-1
    return -1

arr=[2,4,6,8.10]
print(interpolationSearch(arr,8))





