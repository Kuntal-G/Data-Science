# Retreive K random lements from array of unbounded size
import random
def reservoirSampling(arr,k):
    
    reservoir=[]
    
    for i , item in enumerate(arr):
        
        if i<k:
            reservoir.append(item)
        else:
            m=random.randint(0,i)
            if m<k:
                reservoir[m]=item
                
    return reservoir


arr=[2,3,4,6,7,12,34,56,2,3]
print(reservoirSampling(arr,20))
        

