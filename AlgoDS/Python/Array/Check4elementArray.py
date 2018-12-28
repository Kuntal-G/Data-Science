#Check whether array has four elements such that a+b=c+d

def check_four_elements(arr,operation='product'):
    
    kv_store={}
    n=len(arr)
    
    
    if operation=='add':
        
        for i in range (n-1):
            for j in range (i+1, n):
                
                sum_val=arr[i]+arr[j]
                
                if sum_val in kv_store:
                    prev_element=kv_store.get(sum_val)
                    print((arr[i],arr[j]),prev_element)
                
                else:
                    
                    kv_store[sum_val]=(arr[i],arr[j])
    else:
        
        for i in range (n-1):
            for j in range (i+1, n):
                
                prod_val=arr[i]*arr[j]
                
                if prod_val in kv_store:
                    prev_element=kv_store.get(prod_val)
                    print((arr[i],arr[j]),prev_element)
                
                else:
                    
                    kv_store[prod_val]=(arr[i],arr[j])
                    
                

arr = [3, 4, 7, 1, 2, 9, 8] 

check_four_elements(arr,'add')
