# Reverse words in a String and also reverse individual words.

def reverseWordsInString(str):
    
    return str.split(' ')[::-1]

def reverseIndividualWords(str):
    output=[]
    for word in str.split(' '):
        output.insert(0,word[::-1])
    return output
        

str='My name is Kuntal'

print(reverseWordsInString(str))
print(reverseIndividualWords(str))

