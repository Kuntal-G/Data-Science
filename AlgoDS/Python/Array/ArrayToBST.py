#Sorted array or list to BST

class TreeNode:
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        

def sorted_array_bst(arr):
    
    if not arr:
        return None
    
    mid=len(arr)//2
    
    root=TreeNode(arr[mid])
    
    root.left=sorted_array_bst(arr[:mid])
    
    root.right=sorted_array_bst(arr[mid+1:])
    
    return root

def pre_order_traversal(node):
    
    if not node:
        return None
    
    print(node.data)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

print('===========')
arr = [1, 2, 3, 4, 5, 6, 7] 
node=sorted_array_bst(arr) 
pre_order_traversal(node)  
print('===========')
# Container most water
