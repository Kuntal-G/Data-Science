# Calculate the product of array without itself

def product_except_self(arr):
    
    size = len(arr)
    output = [1] * size
    left = 1
    

    for x in range(size - 1):

        left *= arr[x]
        output[x + 1] *= left

        
    
    right = 1
    
    
    for x in range(size - 1, 0, -1):

        right *= arr[x]
        output[x - 1] *= right

        
    return output

arr=[10, 3, 5, 6, 2]
print(product_except_self(arr))
        
    

