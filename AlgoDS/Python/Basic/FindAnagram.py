#find the size of largest subset of anagram words

from collections import Counter

def maxAnagramSize(input):

    input=input.split(" ")

    for i in range(0,len(input)):
        input[i]= ''.join(sorted(input[i]))

    print(input)
    count=Counter(input)

    return max(count.values())


input = 'ant magenta magnate tan gnamate'
print(maxAnagramSize(input))