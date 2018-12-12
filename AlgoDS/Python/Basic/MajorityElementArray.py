#Check majority element in array

from collections import Counter
def findMajority(arr):

    count=Counter(arr)

    return max(count.values(),key=count.get)

arr=[5, 3, 5, 0, 5, 0, 5,0]
#print(findmajority(arr))


#without hash/counter- using boyer-moore voting


def majorityElem(arr):

    maxIndex=0
    count = 1
    for i in range(len(arr)):
        print(i,arr[i])
        if count == 0:
            
            maxIndex = i
            count +=1
            
        elif arr[maxIndex] == arr[i]:
            count += 1
            
        else:
            count -= 1
            

    return arr[maxIndex]

print(majorityElem(arr))