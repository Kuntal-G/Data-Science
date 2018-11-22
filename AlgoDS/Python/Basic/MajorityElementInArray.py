#Check majority element in array

from collections import Counter
def findMajority(arr):

    count=Counter(arr)

    return max(count.values(),key=count.get)

arr=[5, 3, 5, 0, 5, 0, 5,0]
#print(findmajority(arr))


#without hash/counter- using boyer-moore voting


def majorityElem(input):

    candidate = 0
    count = 0
    for value in input:
        if count == 0:
            candidate = value
        if candidate == value:
            count += 1
        else:
            count -= 1

    return candidate

print(majorityElem(arr))