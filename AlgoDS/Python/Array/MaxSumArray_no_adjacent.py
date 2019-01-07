#Maximum Sum no adjacent element


def max_no_adjacent(arr):
    
    incl=0
    excl=0
    
    for i in arr:
        
        new_excl=max(incl,excl)
        incl=excl+i
        excl=new_excl
        
    return max(incl,excl)

arr = [5, 5, 10, 100, 10, 5] 
print(max_no_adjacent(arr))

