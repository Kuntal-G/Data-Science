#Longest common subsequence between two string
"""
Created on Tue Dec 25 13:47:55 2018

@author: kuntalg
"""

def longest_common_sub_sequence(s1,s2):
    
    m=len(s1)
    n=len(s2)
    
    L=[[None]* (n+1) for j in range(m+1)]
    
    
    for i in range(m+1):
        for j in range(n+1):
            
            
            
            if i==0 or j==0:
                L[i][j]=0
                
            #When characters are same use the value from diagonal above +1     
            elif s1[i-1]==s2[j-1]:
                L[i][j]= 1+L[i-1][j-1]
                
                
            else:
                #When characters are different use the maximum
                # of the two diagonal value on left
                L[i][j]= max(L[i-1][j],L[i][j-1])
                
            
            
            
    index=L[m][n]
    lcs= [""]*(index+1)
    lcs[index]=""
    
    i=m
    j=n
    
    while i>0 and j>0:
        
        if s1[i-1]==s2[j-1]:
            lcs[index-1]=s1[i-1]
            i-=1
            j-=1
            index-=1
        elif L[i-1][j]>L[i][j-1]:
            i-=1
        else:
            j-=1
        
    
    
                
    return L[m][n],"".join(lcs)

X = "AGGTAB"
Y = "GXTXAYB"
print ("Length and  LCS is ", longest_common_sub_sequence(X, Y) )
                
    
    