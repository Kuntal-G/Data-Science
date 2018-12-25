# Peak element in an array

def peak_elements(arr):
    
    peakElem=arr[0]
    
    for i in range(1, len(arr)):
        
        if arr[i]>peakElem:
            peakElem=arr[i]
            
    return peakElem

arr=[1,5,2,3,1]

print(peak_elements(arr))