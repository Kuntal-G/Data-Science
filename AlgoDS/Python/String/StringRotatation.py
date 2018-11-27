# String and array rotation-- left right

def stringRotation(str,k=1,type='right'):

    k=k % len(str)
    print(k)

    if type=='left':

        return str[k:]+str[:k]

    elif type=='right':

        return str[-k:]+str[:-k]

    return str

str='abcdef'
str1=[1,2,3,4,5]

print(stringRotation(str1,4,'left'))


