#Kth Largest element in an array
import heapq
def kth_largest(arr,k):
    
    heap=[]
    
    for elem in arr:
        heapq.heappush(heap,-elem)
        
    for _ in range(k):
        
        result=heapq.heappop(heap)
    
    return -result
        
a=[3,2,1,5,6,4]
print(kth_largest(a,2))
