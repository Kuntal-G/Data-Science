#Matrix Mirror sum
def sum_matrix_mirror(mat):
    
    #assumming matrix is square nxn
    #although similar logic will work for mxn matrix as well
    n=len(mat)

    
    for i in range(n):
        for j in range(n):
            
            print(mat[i][j]+mat[i][n-1-j],end=" ")
        print(" ")
            


matrix =[ 
            [ 1, 2, 3,], 
            [ 4, 5, 6 ], 
            [ 7, 8, 9 ], 
        ]
            
print(sum_matrix_mirror(matrix))       
       
