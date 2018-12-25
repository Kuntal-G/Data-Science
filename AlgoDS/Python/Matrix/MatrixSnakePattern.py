# Snake pattern matrix

def snake_pattern(mat):
    n=len(mat)
    
    for row in range(n):
            #even row left->right
            if row%2==0:
                for col in range(n):
                    print(mat[row][col],end =" ")
                    
            else: #odd row right->left
                for col in range(n-1,-1,-1):
                    print(mat[row][col],end =" ")
            
                
             

matrix =[ 
            [ 1, 2, 3,], 
            [ 4, 5, 6 ], 
            [ 7, 8, 9 ], 
        ]

snake_pattern(matrix)