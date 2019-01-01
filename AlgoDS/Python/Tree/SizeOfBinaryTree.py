#Size of a binary tree

class TreeNode:
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def size_binary_tree(node):
    
    if node is None:
        return 0
    else:
        return (size_binary_tree(node.left)+1+size_binary_tree(node.right))

root = TreeNode(10);  
root.left = TreeNode(20);  
root.right = TreeNode(30);  
root.left.left = TreeNode(40);  
root.left.right = TreeNode(50);  

print(size_binary_tree(root))
