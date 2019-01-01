# Deepest sum binary search tree
class TreeNode:
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def deep_sum_bst(node, depth=0,current=0):
    
    if not node:
        return (depth,current)
    
    depth +=1
    current +=node.data
    
    return max(deep_sum_bst(node.left,depth,current),deep_sum_bst(node.right,depth,current))


root =  TreeNode(1)
root.left =  TreeNode(2)
root.right =  TreeNode(3) 
root.left.left =  TreeNode(4) 
root.left.right =  TreeNode(5) 
root.right.left =  TreeNode(6) 
root.right.right =  TreeNode(7)

print(deep_sum_bst(root))
