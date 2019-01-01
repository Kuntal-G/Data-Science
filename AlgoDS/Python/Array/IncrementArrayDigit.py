#Add 1 to diigits in array

def increment_digit_array(arr):
    
    n=len(arr)
    
    arr[n-1]+=1
    carry=arr[n-1]/10
    arr[n-1]=arr[n-1]%10
    
    
    for i in range (n-2,-1,-1):
        if carry==1:
            arr[i]+=1
            carry=arr[i]/10
            arr[i]=arr[i]%10
    
    if carry==1:
        arr.insert(0,1)
    
    return arr

print(increment_digit_array([9,3,9]))
        
        