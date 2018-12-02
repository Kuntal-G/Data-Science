# Kth non-repeating element

def k_NonRepeating(str,k):
    
    return [s for s in str if str.count(s)==1][:k]

# This could also be done using dictionary to maintain the count instead od string count.
    

str='geeksforgeeks'

print(k_NonRepeating(str,3))


