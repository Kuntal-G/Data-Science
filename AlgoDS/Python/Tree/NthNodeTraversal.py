#Nth order/node traversal inorder

class TreeNode:
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        



def nth_node_traversal(node,n):
    
    if node is None:
        return 
    
    count=1
    if count<=n:
        nth_node_traversal(node.left,n)
        count+=1
        
        
        if count==n:
            print(node.data)
           
        
        nth_node_traversal(node.right,n)
        
        
    
    
root = TreeNode(10);  
root.left = TreeNode(20);  
root.right = TreeNode(30);  
root.left.left = TreeNode(40);  
root.left.right = TreeNode(50);  
    
n = 4;  
    
nth_node_traversal(root, n);  