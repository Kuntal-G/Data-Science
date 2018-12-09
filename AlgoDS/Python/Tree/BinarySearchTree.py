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
            
        
    def search(self,key):
        if key < self.data:
            if self.left is None:
                return str(key)+" Not Found"
            return self.left.search(key)
        elif key > self.data:
            if self.right is None:
                return str(key)+" Not Found"
            return self.right.search(key)
        else:
            print(str(self.data) + ' is found')    
        
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
                    
                
            
root = TreeNode(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.print_tree() 

print(root.search(3))      
        

