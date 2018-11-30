# Remove Duplicate from List

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
            
    def removeDuplicate(self):
        
        current=self.head
        next_next=None
        
        while(current.next is not None):
            
            if(current.data == current.next.data):
                next_next=current.next.next
                current.next=None
                current.next=next_next
            else:
                current=current.next

if __name__== '__main__':
    
    ll=LinkedList()
    ll.insertBegining(1)
    ll.insertBegining(2)
    ll.insertBegining(2)
    ll.insertBegining(3)
    ll.insertBegining(4)
    ll.insertBegining(6)
    ll.insertEnd(5)
    ll.printList()
    print('Removing Duplicate')
    ll.removeDuplicate()
    ll.printList()
    
    
            
    
    
    
    

