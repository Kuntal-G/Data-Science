#Find the maximum j – i such that arr[j] > arr[i]


def max_difference_ji(arr):
    #Brute force O(n2)
    n=len(arr)
    maxDiff=-1
    for i in range(n):
        j=n-1
        
        while j>i:
            if arr[j]>arr[i] and maxDiff< (j-i):
                maxDiff=j-i
            j-=1
    return maxDiff

arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
print(max_difference_ji(arr))
            
        
    
def max_difference_maximum(arr):
    print('*************')
    n=len(arr)
    Lmin=[0]*n
    Rmax=[0]*n
    
    Lmin[0]=arr[0]
    Rmax[n-1]=arr[n-1]
    

    
    for i in range(1,n):
        Lmin[i]=min(arr[i],Lmin[i-1])
        
    
    for j in range(n-2,-1,-1):
        Rmax[j]=max(arr[j],Rmax[j+1])
        
    i,j=0,0
    maxDiff=-1
    
    

    while i<n and j<n:
        
        if Lmin[i]<Rmax[j]:
            
            maxDiff=max(maxDiff, j-i)
            
            j+=1
        else:
            i+=1
        
    
     
    return maxDiff
print(max_difference_maximum(arr))        
    
