def uniqueNum(arr):
    
    res=0
    
    for num in arr:
        
        res^=num
        
    
    return res

ar=[2,3,2,4,3,1,1]
print(uniqueNum(ar))