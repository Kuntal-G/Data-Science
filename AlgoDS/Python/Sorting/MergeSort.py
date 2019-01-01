#Merge sort implementation O(NlogN)

def merge(a,b):

    (m,n)=(len(a),len(b))

    i=j=0
    k=[]

    while i<m and j<n:

        if a[i]<=b[j]:
            k.append(a[i])
            i +=1
        else:
            k.append(b[j])
            j +=1

    while i<m:
        k.append(a[i])
        i += 1

    while j<n:
        k.append(b[j])
        j += 1

    return k


def mergeSort(x):

    if len(x)>1:
        mid= len(x)//2
        lefthalf=x[:mid]
        righthalf=x[mid:]

        half_a=mergeSort(lefthalf)
        half_b=mergeSort(righthalf)

        x=merge(half_a,half_b)

    return x

arr=[6,4,8,2,13,9]
print(mergeSort(arr))


#merge 3 sorted array
A = [1, 2, 3, 5]
B = [6, 7, 8, 9]

print(merge(A,B))


#Merge using heapq

from heapq import merge

sortedarr=list(merge(A,B))

print(sortedarr)