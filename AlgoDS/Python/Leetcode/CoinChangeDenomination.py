#Coin change with denomination sum

def coin_change(S, target): 
  
    m=len(S)
    table = [0 for k in range(target+1)] 
  
    # Base case (If given value is 0) 
    table[0] = 1
  
    
    
    for i in range(0,m): 
        
        for j in range(S[i],target+1): 
            
            table[j] += table[j-S[i]] 
            
            
            
            
    
    return table[target] 
  

arr = [1, 2, 3] 
coin_change(arr,4)
                
                    
  
