#Search Middle Node and Kth Node from Last in Linked List

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
            
    def findMiddleElement(self):
        
        slow_ptr=self.head
        fast_ptr=self.head
        
        while(fast_ptr is not None and fast_ptr.next is not None):
            fast_ptr=fast_ptr.next.next
            slow_ptr=slow_ptr.next
        
        print('The middle node value is {}'.format(slow_ptr.data))
        
        
    def kthNodeFromLast(self,k):
        
        slow_ptr=self.head
        fast_ptr=self.head
        
        count=0
        
        #this will take the fast_ptr to kth node from begining
        while (count<k and fast_ptr is not None):
            fast_ptr=fast_ptr.next
            count +=1
        
        #Now fast_ptr is in kth node from begining. It will move from kth to last node (let say n)
        # And the slow_ptr will reach N-K from begining, which is the kth node from end.
        while (fast_ptr is not None):
            fast_ptr=fast_ptr.next
            slow_ptr=slow_ptr.next
        return 'Kth node from End is {}'.format(slow_ptr.data)
        

if __name__== '__main__':
    
    ll=LinkedList()
    ll.insertBegining(1)
    ll.insertBegining(2)
    ll.insertBegining(3)
    ll.insertBegining(4)
    ll.insertEnd(5)
    ll.insertEnd(6)
    ll.printList()
    ll.findMiddleElement()
    print(ll.kthNodeFromLast(2))
    
    
            
    
    
    
    
