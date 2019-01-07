# Minimum cost path matrix to (m,n)cell


def min_cost_path(mat,m,n):
    
    rows=len(mat)
    cols=len(mat[0])
    
    tc=[[0 for x in range(cols)] for x in range(rows)]
    
    tc[0][0]=mat[0][0]
    
    # Update the first row of the total cost matrix (tc)
    
    for col in range(1,cols):
        tc[0][col]=tc[0][col-1] + mat[0][col]
    
    
    # Update first column of the total cost matrix (tc)
    for row in range(1,rows):
        tc[row][0]=tc[row-1][0] + mat[row][0]
        
    # Update the current cell base don the min value of top,left,diagonal
    for row in range(1,rows):
        
        for col in range(1,cols):
            
            tc[row][col]=min(tc[row-1][col],tc[row][col-1],tc[row-1][col-1])+mat[row][col]
      
    return tc[m][n]

cost = [[1, 2, 3], 
        [4, 8, 2], 
        [1, 5, 3]] 
print(min_cost_path(cost, 2, 2)) 
    
    
    
