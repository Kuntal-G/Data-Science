# Minimum eidt distance between two string
"""
Created on Tue Dec 25 13:47:55 2018

@author: kuntalg
"""

def edit_distance_two_string(s1,s2):
    
    m=len(s1)
    n=len(s2)
    
    L=[[0 for i in range(n+1)] for j in range(m+1)]



    
    for i in range(m+1):
        for j in range(n+1):
            
            
            #null string on one side, will take all edit of other string
            if i==0:
                L[i][j]=j
             
            #same for column
            elif j==0:
                L[i][j]=i
            
            #When characters are same use the value from diagonal above,nothing to edit
            elif s1[i-1]==s2[j-1]:
                L[i][j]= L[i-1][j-1]
                

                
            else:
                #When characters are different 
                #use the value of the minimum between (left,up,l-diagonal)+1
            
                L[i][j]=1+ min(L[i][j-1],L[i-1][j],L[i-1][j-1])
    
           
    

                
    return L[m][n]

X = 'sunday'
Y = 'monday'
                
                
print(edit_distance_two_string(X,Y))    
