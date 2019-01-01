#Lowest common ancestor Binary tree and bst
class TreeNode:
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        


#LCA binary tree

def lca_binary_tree(node,n1,n2):
    
    if node is None:
        return None
    
    if node.data==n1 or node.data==n2:
        return node.data
    
    
    left_lca=lca_binary_tree(node.left,n1,n2)
    right_lca=lca_binary_tree(node.right,n1,n2)
    
    # when both the above subtree call is not none, then one key on left and other right, hence lca is current node
    if left_lca !=None and right_lca !=None:
        
        return node.data
    
    return left_lca if left_lca !=None else right_lca

root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
root.right.left = TreeNode(6) 
root.right.right = TreeNode(7)
    
print(lca_binary_tree(root,4,5))
print(lca_binary_tree(root,4,6))
    

#LCA binary search tree

def lca_bst(node,n1,n2):
    
    if node is None:
        return None
    
    #Root greater than both values means the lca in left subtree
    if node.data>n1 and root.data>n2:
        return lca_bst(node.left,n1,n2)
    
    #Root lesser than both values means the lca in right subtree
    if node.data<n1 and node.data<n2:
        return lca_bst(node.right,n1,n2)
    
    return node.data


root1 = TreeNode(20) 
root1.left = TreeNode(8) 
root1.right = TreeNode(22) 
root1.left.left = TreeNode(4) 
root1.left.right = TreeNode(12) 
root1.left.right.left = TreeNode(10) 
root1.left.right.right = TreeNode(14) 

print(lca_bst(root1,14,8))