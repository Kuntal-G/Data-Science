# Basic LinkedList operation

class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    
    def __init__(self):
        self.head=None
        
    def insertBegining(self,data):
        
        newNode=Node(data)
        
        newNode.next=self.head
        self.head=newNode
        
        return 'Inserted data {} in the begining of list'.format(data)
    
    
    def insertEnd(self,data):
        
        newNode=Node(data)
        
        if self.head is None:
            
            self.head=newNode
            
        last=self.head
        
        while(last.next):
            last=last.next
            
        last.next=newNode
        
        return 'Inserted data {} in the end of list'.format(data)
    
    def printList(self):
        
        current=self.head
        while (current):
            print(current.data)
            current=current.next

if __name__== '__main__':
    
    ll=LinkedList()
    ll.insertBegining(1)
    ll.insertBegining(2)
    ll.insertBegining(3)
    ll.insertBegining(4)
    ll.insertEnd(5)
    ll.printList()
    
    
            
    
    
    
    