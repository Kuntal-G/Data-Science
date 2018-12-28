#Search sorted matrix

def search_matrix(mat,elem):
    
    n=len(mat[0])
    
    i=0
    j=n-1
    
    while i<n and j>=0:
        
        if mat[i][j]==elem:
            
            print('Found at position',(i,j))
            return True
            
        elif mat[i][j]>elem:
            j-=1
        else:
            i+=1
    print ('Not found')
    return False

mat= [ [10, 20, 30, 40,60], 
        [15, 25, 35, 45,52], 
        [27, 29, 37, 48,75], 
        [32, 33, 39, 50,69] ] 

search_matrix(mat,39)
