#Reverse String of words

def reverseStringOfWords(str):

    str=str.split(" ")

    str=str[::-1]


    return " ".join(str)

input="My name is Kuntal"

print(reverseStringOfWords(input))



