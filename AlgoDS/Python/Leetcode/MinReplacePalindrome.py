#Minimum character replace to make string palindrome

def min_replace_palindrome(s):
    
    n=len(s)
    if n==1:
        return 0
    
    min_replace=0
    
    for i in range(n//2):
        
        if s[i]==s[n-i-1]:
            continue
        
        min_replace+=1
        
        if s[i]<s[n-i-1]:

            s[n-i-1]=s[i]
        else:

            s[i]=s[n-i-1]
     
    #print(*s,end='')    
    return min_replace, s

print(min_replace_palindrome(list('geeks')))
            
