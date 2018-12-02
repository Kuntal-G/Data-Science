# Sort array of 0,1 and 2

def sortZeroOneTwo(arr):
    
    low=0
    mid=0
    high=len(arr)-1
    
    while mid<=high:
        
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    
    return arr

arr=[0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] 
print(sortZeroOneTwo(arr))

