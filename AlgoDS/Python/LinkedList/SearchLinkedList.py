# Search Element in a LinkedList

class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    
    def __init__(self):
        self.head=None
        
    def push(self,data):
        
        node=Node(data)
        node.next=self.head
        self.head=node
        
    def printList(self):
        
        current=self.head
        while (current):
            print(current.data)
            current=current.next
        
    def searchElement(self,key):
        
        current=self.head
        
        while (current is not None):
            
            if current.data==key:
                return 'Data Found in the Linked List'
            current=current.next
            
        return 'Data not found in the LinkedList'
    

if __name__=='__main__':
    
    ll=LinkedList()
    ll.push(3)
    ll.push(2)
    ll.push(4)
    ll.push(1)
    ll.push(5)
    ll.printList()
    print(ll.searchElement(2))
