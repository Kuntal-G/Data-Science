#Third largest in an array

import sys 
def third_largest(arr): 
  

    first = arr[0] 
    second = -sys.maxsize 
    third = -sys.maxsize 
  
    # Traverse array elements 
    # to find the third Largest 
    for i in range(1, len(arr)): 
      
        if (arr[i] > first): 
          
            third = second 
            second = first 
            first = arr[i] 
            
        elif (arr[i] > second): 
          
            third = second 
            second = arr[i] 
           
        elif (arr[i] > third): 
            third = arr[i] 
      
    return third
    
  

arr = [12, 13, 110, 34, 16] 
n = len(arr) 
print(third_largest(arr) )
  