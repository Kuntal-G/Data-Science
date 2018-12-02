#Check whether array has consecutive number

def checkContinousNum(arr,approach):
    #O(n) --min max function can be done with linear scan
    if approach=='min-max':
        max_elem=max(arr)
        min_elem=min(arr)
        arr_size=len(arr)
        
        if (max_elem - min_elem)+1 == arr_size:
            return True
        else:
            return False
    
    else: #O(nlongn) for sort
        arr.sort()
        for i in range(1,len(arr)):
            
            if abs(arr[i] - arr[i-1]) >1:
                return False
        return True
    
arr=[5,9,7,8]
print(checkContinousNum(arr,'min-max'))
