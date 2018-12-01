# Find the 3 elements whose sum corresponds to target

def threeSums(arr,target):
    arr=sorted(arr)
    
    for i in range(0, len(arr)-2):
        
        l=i+1
        r=len(arr)-1
        
        while l<r:
            
            if arr[i] +arr[l]+arr[r]==target:
                print(i,l,r)
                
                return (arr[i],arr[l],arr[r])
            
            elif arr[i] +arr[l]+arr[r]<target:
                l+=1
            
            else:
                r-=1
            
    return False
    
arr=[1,4,6,7,8]


print(threeSums(arr,14))
    

