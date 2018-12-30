#O(N2) using two loops possible.
#Next greater element in array  
#O(N) time with O(N) space implentation. 

def next_greater_element(arr):
    
    stack=[]
    
    stack.append(arr[0])
    next_elem=0
    
    for i in range(1,len(arr)):
        
        next_elem=arr[i]
        
        if len(stack)>0:
            element=stack.pop()
            
            while element<next_elem:
                
                print(str(element)+'--->'+str(next_elem))
                
                if len(stack)==0:
                    break
                element=stack.pop()
                
            if element>next_elem:
                stack.append(element)
        
        stack.append(next_elem)
            
    while len(stack)!=0:
        
        next_elem=-1
        element=stack.pop()
        print(str(element)+'--->'+str(next_elem))

arr = [11, 13, 21, 3] 

#Next smaller element in an array. 
 
def next_smaller_element(arr):
    
    stack=[]
    
    stack.append(arr[0])
    next_elem=0
    
    for i in range(1,len(arr)):
        
        next_elem=arr[i]
        
        if len(stack)>0:
            element=stack.pop()
            
            while element>next_elem:
                
                print(str(element)+'--->'+str(next_elem))
                
                if len(stack)==0:
                    break
                element=stack.pop()
                
            if element<next_elem:
                stack.append(element)
        
        stack.append(next_elem)
            
    while len(stack)!=0:
        
        next_elem=-1
        element=stack.pop()
        print(str(element)+'--->'+str(next_elem))
   
next_smaller_element(arr)




