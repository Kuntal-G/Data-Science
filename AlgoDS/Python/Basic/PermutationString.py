#Check if one string is permutation of other

def checkPermutation(s1,s2):

    sum=0
    for ch in s1:
        sum += ord(ch)

    for ch in s2:
        sum -=ord(ch)

    return sum==0

print(checkPermutation('dog','gods'))

