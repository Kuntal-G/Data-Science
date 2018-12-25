#Union Intersection of array

def array_union_intersection(a1,a2, perform='union'):
    
    #we can do basic check of size of zero or 1 element
    #Also if unsorted array then we can first sort and 
    #then use the below technique.
    
    m=len(a1)
    n=len(a2)
    
    i,j=0,0
    
    result=[]
    if perform=='intersection':
        
        while i<m and j<n:
            if a1[i]==a2[j]:
                result.append(a1[i])
                i+=1
                j+=1
            
            elif a1[i]<a2[j]:
                i+=1
            else:
                j+=1
                
    else:
        
        while i<m and j<n:
            if a1[i]==a2[j]:
                result.append(a1[i])
                i+=1
                j+=1
            
            elif a1[i]<a2[j]:
                result.append(a1[i])
                i+=1
            else:
                result.append(a2[j])
                j+=1
        
        while i<m:
            result.append(a1[i])
            i+=1
            
        while j<n:
            result.append(a2[j])
            j+=1
        
        
        
        
    return result

a1=[1,3,4,5,6]
a2=[3,6,8,9,10]


print(array_union_intersection(a1,a2,perform='intersection'))
            


