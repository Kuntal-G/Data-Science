#Maximum Contiguous array using DP & Kadane

def max_value(a,b):
    
    if a>b:
        return a
    else:
        return b
    

def long_sum_continuous(arr):
    
    max_sum=arr[0]
    current_sum=arr[0]
    
    for i in range(1,len(arr)):
        current_sum=max_value(arr[i],current_sum+arr[i])
        max_sum=max_value(max_sum,current_sum)
        
    return max_sum

a = [-2, -3, 4, -1, -2, 1, 5, -3] 
print(long_sum_continuous(a))

#another variation of continous sum with index(start-end)

def max_sum_continous(arr):
    
    current_so_far=0
    max_sum=0
    
    start=0
    end=0
    s=0
    
    for i in range(len(arr)):
        
        current_so_far=current_so_far+arr[i]
        
        if current_so_far<0:
            current_so_far=0
            s=i+1
            
        if max_sum<current_so_far:
            max_sum=current_so_far
            start=s
            end=i
            
    return max_sum,(start,end)
        
print(max_sum_continous(a))    
    
