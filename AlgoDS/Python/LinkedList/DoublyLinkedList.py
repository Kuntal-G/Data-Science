# Doubly LinkedList implementation

class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
        
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head=None
        
    #insert in the beginning    
    def push(self,data):
        
        node=Node(data)
        
        node.next=self.head
        node.prev=None
        
        if self.head is not None:
            self.head.prev=node
            
        self.head=node
        
    #insert at the end
    def append(self,data):
        
        node=Node(data)
        node.next=None
        
        if self.head is None:
            node.prev=None
            self.head=node
        else:
            last=self.head
            
            while last.next is not None:
                last=last.next
            
            last.next=node
            node.prev=last
            
            
    
    
    
    
    
    # Print list element both ways
    
    def print_list(self):
        
        current=self.head
        last=None
        print('Forward Traversal')
        while (current is not None):
            last=current
            print(current.data)
            current=current.next
            
        print('Backward Traversal')
        while (last is not None):
            print(last.data)
            last=last.prev
            
            
dl=DoublyLinkedList()
dl.push(1)   
dl.push(2) 
dl.push(3) 
dl.append(4)
print(dl.print_list())    
        