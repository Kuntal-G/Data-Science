#Print diagonals of a matrix

def print_diagonal(mat):
    
    n=len(mat)
    #diagonal
    print('Diagonal Elements')
    for i in range(n):
        print (mat[i][i])
        
    
    #Reverse diagonal
    print('Reverse Diagonal Elements')
    
    for i in range(n):
        print (mat[i][n-1- i])
    

matrix =[ 
            [ 1, 2, 3,], 
            [ 4, 5, 6 ], 
            [ 7, 8, 9 ], 
        ]


print_diagonal(matrix)