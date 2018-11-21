# Duplicate characters in a string


from collections import Counter

def dupCharinString(str):

    count=Counter(str)

    for key,val in count.items():

        if val>1:
            print(key)


input = 'hellobrother'
dupCharinString(input)




