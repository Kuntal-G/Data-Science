# Kth Smallest and Largest elemenst in array

# Using  Heap 
import heapq

def findKthLargestOrSmallest_Heap(arr,k,note='largest'):
    
    heap=[]
    
    if note=='smallest':
        
        for num in arr:
            heapq.heappush(heap,num)
        print(heap)
        for _ in range(k):
            res=heapq.heappop(heap)
        
        return res
    else:
        for num in arr:
            heapq.heappush(heap,-num)
        print(heap)
        for _ in range(k):
            res=heapq.heappop(heap)
        
        return res * -1
        
l=[2,4,6,1,67,13,4,56] 

print(findKthLargestOrSmallest_Heap(l,2,'smallest'))  


# Using Sort

def findKthLargestOrSmallest(arr,k,note='largest'):
    arr.sort()
    
    if note=='smallest':
        return arr[:k]
    else:
        return arr[k:]
    
arr = [12, 3, 5, 7, 19] 

#print(findKthLargestOrSmallest(arr,2,'smallest'))



