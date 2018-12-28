#Intersection between two array
def array_intersection(a,b):
    
    a.sort()
    b.sort()
    
    index_a=0
    index_b=0
    result=[]
    
    while index_a<len(a) and index_b<len(b):
        
        if a[index_a]==b[index_b]:
            result.append(a[index_a])
            index_a+=1
            index_b+=1
        elif a[index_a]>b[index_b]:
            index_b+=1
        else:
            index_a+=1
    return result

a=[2,3,4,8,5]
b=[2,2,3]

print(array_intersection(a,b))

