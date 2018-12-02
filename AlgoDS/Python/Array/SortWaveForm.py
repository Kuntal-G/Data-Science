# Sort Array in Wave form such that: if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >=..


def sortWaveForm(a):
    
    for i in range(0,len(arr)-1,2):
        
        if i>0 and a[i]<a[i+1]:
            a[i],a[i-1]=a[i-1],a[i]
        if i < len(arr)-2 and a[i]<a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    return a
            


arr=[10, 90, 49, 2, 1, 5, 23] 
print(sortWaveForm(arr))


