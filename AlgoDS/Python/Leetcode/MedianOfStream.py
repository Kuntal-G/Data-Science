# Median of a stream of unsorted numbers
import heapq
class MedianFinder:
    
    def __init__(self):
        self.max_heap=[]
        self.min_heap=[]
    
    def add_stream(self, num):
        
        if not self.max_heap or num > -self.max_heap[0]:
            heapq.heappush(self.min_heap,num)
            
            if len(self.min_heap)>len(self.max_heap)+1:
                heapq.heappush(self.max_heap,-heapq.heappop(self.min_heap))
        else:
            heapq.heappush(self.max_heap,-num)
            
            if len(self.max_heap)>len(self.min_heap)+1:
                heapq.heappush(self.min_heap,-heapq.heappop(self.max_heap))
                
    
    def find_median(self):
        
        if len(self.min_heap)==len(self.max_heap):
            
            return (-self.max_heap[0]+self.min_heap[0])/2.0
        else:
            return self.min_heap[0]
            
        
arr=[5,10,15]

obj = MedianFinder()

for num in arr:
    obj.add_stream(num)  
    print(obj.find_median())
     