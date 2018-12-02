# Permutation of a String

from itertools import permutations

def stringPermutation(str):
    
    return [''.join(perm) for perm in permutations(str)]

#Recursive way of doing it
def permuteRecursive(string):
    
    permutation_list=[]
    if len(string)==1:
        return string
    else:
        for s in string:
            [permutation_list.append(s+a) for a in permuteRecursive(string.replace(s,""))]
            
        
    return permutation_list


print(stringPermutation('abc'))
print(permuteRecursive('abc'))
    




