# Minimum Element in sorted rotated array

def find_min(num):
    
    if num[0] < num[-1]:
        return num[0]
    elif len(num)<=5:
        return min(num)
    else:
        mid = (len(num)) // 2
        return min(find_min(num[:mid]), find_min(num[mid:]))

arr = [4,5,6,0,7,1,2]

print(find_min(arr))