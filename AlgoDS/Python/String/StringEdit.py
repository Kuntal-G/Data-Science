#Check if the edit distance between two string is more than 1


def checkStringEdit(str1,str2):

    count=0
    i=0
    j=0

    m=len(str1)
    n=len(str2)

    if abs(m-n)>1:
        return False


    while (i<m and j<n):

        if str1[i]!=str2[j]:

            if count==2:
                return False

            if m>n:
                i+=1
            elif n>m:
                j+=1
            else:

                i+=1
                j+=1


            count +=1

        else:
            i+=1
            j+=1



    if i<m or j<n:
        count +=1

    return count ==1


str1='pales'
str2='pale'

print(checkStringEdit(str1,str2))


data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)]

def test(data):
    for item in data:

        print(checkStringEdit(item[0],item[1])==item[2], item)

# Find one string permutation of other


print(test(data))