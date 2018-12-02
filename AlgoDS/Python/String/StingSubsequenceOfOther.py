# One string is subsequence of other string

def checkStringSubsequence(str1,str2):
    
    i=0
    j=0
    m=len(str1)
    n=len(str2)
    
    while i<m and j<n:
        
        if str1[i]==str2[j]:
            i+=1
        j+=1
        
    return i==m

str1 = "AXY"
str2 = "ADXCPY"

print(checkStringSubsequence(str1,str2))

