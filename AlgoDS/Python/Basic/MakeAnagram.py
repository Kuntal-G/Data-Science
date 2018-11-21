# Min character to be removed to make two string anagram

def makeAnagram1(a, b):

    buffer=[0]*26

    for c in a:
        buffer[ord(c)-ord('a')] +=1

    for c in b:
        buffer[ord(c) - ord('a')] -= 1

    return sum(map(abs,buffer))


from collections import Counter
def makeAnagram2(a,b):

    count1=Counter(a)
    count2 = Counter(b)

    key1=count1.keys()
    key2=count2.keys()

    keyset=set(key1)
    commonKey=keyset.intersection(key2)

    if commonKey==0:
        return (len(key1) + len(key2))
    else:
        return (max(len(key1),len(key2))- len(commonKey))




str1 = "bcaeh"
str2 = "hea"

print(makeAnagram1(str1, str2))
print(makeAnagram2(str1, str2))