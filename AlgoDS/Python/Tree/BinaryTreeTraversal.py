# Binary Tree Traversal (inorder, pre/post and level order)

# Binary Tree Insertion,Print,Search

class TreeNode:
    
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        
    def insert(self,data):
        
        if self.data:
            
            if data<self.data:
                if self.left is None:
                    self.left=TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right=TreeNode(data)
                else:
                    self.right.insert(data)    
        else:
            self.data=data
            
        
def inorder_traversal(node):# left->root->right
    if node:
        inorder_traversal(node.left)
        print(node.data)
        inorder_traversal(node.right)
            
def pre_traversal(node):# root->left->right
     if node:
         print(node.data)
         pre_traversal(node.left)
         pre_traversal(node.right)
    
def post_traversal(node):# left->right->root
    if node:
        post_traversal(node.left)
        post_traversal(node.right)
        print(node.data)
            
def levelorder_traversal(node):
    if node:
        queue=[]
        queue.append(node)
             
        while(len(queue)>0):
            print(queue[0].data, end=' ' )
            node=queue.pop(0)
                 
            if node.left is not None:
                queue.append(node.left)
                     
            if node.right is not None:
                queue.append(node.right)
        

                
            
root = TreeNode(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)

print("Inorder Result")
inorder_traversal(root)

print("pre_traversal Result")
pre_traversal(root)

print("post_traversal Result")
post_traversal(root)

print("levelorder_traversal Result")
levelorder_traversal(root)

    
        



