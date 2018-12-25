
# Sum of matrix and its surroundings

def matrix_sum_surroundings(mat):
    
    m=len(mat)
    
    mat[m//2][m//2]=mat[m//2-1][m//2]+mat[m//2][m//2-1]+mat[m//2+1][m//2]+mat[m//2][m//2+1]
    
    for i in range(m):
        for j in range(m):
            print(mat[i][j],end=" ")
            
        print(" ")


matrix =[ 
            [ 1, 2, 3,], 
            [ 4, 5, 6 ], 
            [ 7, 8, 9 ], 
        ]
            
      

matrix_sum_surroundings(matrix)
 