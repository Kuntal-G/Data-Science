#Find k hotel bookings

def k_posible_booking(arr,dep,k):
    
    arr.sort()
    dep.sort()
    
    room_needed=1
    result=1
    i=1
    j=0
    
    while i<len(arr) and j<len(dep):
        
        if arr[i]<dep[j]:
            room_needed +=1
            i +=1
            
            if room_needed > result:
                result=room_needed
        
        else:
            room_needed -=1
            j+=1
            
    
    if result >k:
        return True,result
    
    return False,k

arr = [900, 940, 950, 1100, 1500, 1800] 
dep = [910, 1200, 1120, 1130, 1900, 2000] 


print(k_posible_booking(arr,dep,2))
        
