#Atoi implementation

def atoi(s):
    
    res=0
    
    i=0
    sign=1
    if s[0]=='-':
        sign=-1
        i+=1
    
    for j in range(i,len(s)):
        if s[j]>'0' and s[j]<='9': #Non numeric character check
            res=res*10 +(ord(s[j])-ord('0'))
        else:
            return False
    
    return sign*res

print(atoi("-134"))