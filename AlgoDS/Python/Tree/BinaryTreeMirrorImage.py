#Check if two tree is mirror image of each other

class TreeNode:
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        

#Check if two tree mirror image
        
def check_mirror(a,b):
    
    if a is None and b is None:
        return True
    
    if a is None or b is None:
        return True
    
    return (a.data==b.data and check_mirror(a.left,b.right) and check_mirror(a.right,b.left))


root1 = TreeNode(1) 
root2 = TreeNode(1) 
  
root1.left = TreeNode(2) 
root1.right = TreeNode(3) 
root1.left.left = TreeNode(4) 
root1.left.right = TreeNode(5) 

root2.left = TreeNode(3) 
root2.right = TreeNode(2) 
root2.right.left = TreeNode(5) 
root2.right.right = TreeNode(4) 

print(check_mirror(root1,root2))