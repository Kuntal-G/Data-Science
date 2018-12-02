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


#String/Array rotation using modulo logic
def leftRotate(arr,k):

    n=len(arr)
    mod = k % n
    print('mod',mod)
    s = []


    for i in range(n):
        s.append(arr[(mod + i) % n])

    return s

#left rotate variant
def leftRotate2(arr,k):

    n=len(arr)
    s = []

    for i in range(k,k+n):
        s.append(arr[i % n])

    return s


arr = [ 1, 3, 5, 7, 9 ]
print(leftRotate(arr,3))
print(leftRotate2(arr,3))

#Right rotate with modulo
def right_rotate(arr,k):
    s=[]
    n=len(arr)
    for i in range(n):
        s.insert((i+k)%n,arr[i])

    return s
print(right_rotate(arr,3))





