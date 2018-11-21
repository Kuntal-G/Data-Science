#Panagram checking

def checkPanagram(str):

    buffer= [False]*26


    for ch in str.lower():

        if not ch == " ":
            buffer[ord(ch)-ord('a')] =True



    for val in buffer:
        if val == False:
            return "Not Panagram"

    return "Panagram"

#Using set and 1 loop
def checkPanagram2(str):

    str_new=set(str.lower())

    alpha= [ch for ch in str_new if ord(ch) in range(ord('a'),ord('z')+1)]

    if len(alpha)==26:

        return True

    return False

print(checkPanagram2("The quick brown fox jumps over the little lazy dog"))


