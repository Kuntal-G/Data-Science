#Minimumm Railway platform /meeting room  

def minimum_meeting_room(start,end):
    
    #Sort the array with O(nlogn)
    start.sort()
    end.sort()
    
    room_needed=1
    result=1
    
    i=1
    j=0
    
    n=len(start)
    
    while i<n and j<n:
        
        if start[i]<end[j]:
            room_needed+=1
            i+=1
            
            if room_needed>result:
                result=room_needed
        else:
            room_needed-=1
            j+=1
            
    return result
            

arr = [900, 940, 950, 1100, 1500, 1800] 
dep = [910, 1200, 1120, 1130, 1900, 2000] 

print(minimum_meeting_room(arr,dep))
