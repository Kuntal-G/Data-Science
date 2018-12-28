#Kth Frequent Element in Array
import heapq
def kth_frequent_element(arr,k):
    
    Hash={}
    res=[]
    
    for e in arr:
        
        if e in Hash:
            Hash[e]=Hash.get(e)+1
        else:
            Hash[e]=1
    print(Hash)       
    for key in Hash:
        
        if len(res)<k:
            heapq.heappush(res,(Hash[key],key))
        else:
            heapq.heappushpop(res,(Hash[key],key))
    
    print(res[0][1])
    return res[0]
    
arr=[2,3,6,7,4,4,4,6,3,4,3]
#kth_frequent_element(arr,3)

