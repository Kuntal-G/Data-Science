#Minimum and Maximum height of Binary tree

class TreeNode:
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
 

# minimum height of binary tree

def minimum_height(node):
    
    if node is None:
        return 0
    
    if node.left is None and node.right is None:
        return 1
    
    if node.left is None:
        return minimum_height(node.right)+1
    
    if node.right is None:
        return minimum_height(node.left)+1
    
    return min(minimum_height(node.left),minimum_height(node.right))+1
root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 

print(minimum_height(root))
# maximum height of a binary tree
    
def maximum_height(node):
    
    if node is None:
        return 0
    
    if node.left is None and node.right is None:
        return 1
    
    if node.left is None:
        return maximum_height(node.right)+1
    
    if node.right is None:
        return maximum_height(node.left)+1
    
    return max(maximum_height(node.left),maximum_height(node.right))+1

root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 

print(maximum_height(root))

