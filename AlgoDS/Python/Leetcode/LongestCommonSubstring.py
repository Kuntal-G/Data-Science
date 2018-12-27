#Longest common substring
"""
Created on Tue Dec 25 13:47:55 2018

@author: kuntalg
"""

def longest_common_substring(s1,s2):
    
    m=len(s1)
    n=len(s2)
    
    L=[[0 for i in range(n+1)] for j in range(m+1)]
    
    
    result=0



    
    for i in range(m+1):
        for j in range(n+1):
            
            
            
            if i==0 or j==0:
                L[i][j]=0
                
            #When characters are same use the value from diagonal above +1    
            elif s1[i-1]==s2[j-1]:
                L[i][j]= L[i-1][j-1]+1
                result=max(result,L[i][j])
                

            #When characters are different set zero (no match)    
            else:
                
                L[i][j]=0
    
           
    

                
    return result

X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'
                
                
print(longest_common_substring(X,Y))    
