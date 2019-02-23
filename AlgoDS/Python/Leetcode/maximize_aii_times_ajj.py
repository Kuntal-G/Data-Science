#Maximize a[i]+i)*(a[j]+j in array

def max_value(arr):
    (max1, max2) = (0, 0) 
    for i in range(len(arr)): 
        x = arr[i] + i 

        if (x > max1): 
            max2 = max1 
            max1 = x 

        elif (x > max2 and x != max1): 
             max2 = x 
    return(max1*max2) 

print(max_value([4,5,3,1,10]))