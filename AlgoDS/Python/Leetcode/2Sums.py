# Find the 2 elements whose sum corresponds to target

def twoSums(arr,target):
    
    L = sorted(arr)
    i = 0; j = len(L)-1
    while i < j:
        
        if L[i]+L[j] == target:
            return L[i], L[j]
        elif L[i]+L[j] > target:
            j -= 1
        else:
            i += 1
    return -1,-1


    
    
arr=[1,4,6,7,8]

print(twoSums(arr,10))

    

