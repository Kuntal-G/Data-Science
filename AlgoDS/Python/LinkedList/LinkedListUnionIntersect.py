#Union and Intersection between two linked list

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
            
def union_intersection_list(n1,n2,perform='u'):
    
    store={}
    
    if perform=='i':
        
        current=n1.head
        while (current):
            
            if current.data not in store:
                store[current.data]=1
            current=current.next
        
        current=n2.head
        while (current):
            if current.data in store:
                print(current.data)
            current=current.next
            
    else:
        
        current=n1.head
        while (current):
            
            if current.data not in store:
                store[current.data]=1
            current=current.next
        
        current=n2.head
        while (current):
            if current.data not in store:
                store[current.data]=1
            current=current.next
        
        return store

            
        
        
        
    
    

if __name__== '__main__':
    
    ll=LinkedList()
    ll.insertBegining(1)
    ll.insertBegining(2)
    ll.insertBegining(3)
    ll.insertBegining(4)
    ll.insertEnd(5)
    
    l2=LinkedList()
    l2.insertBegining(1)
    l2.insertBegining(4)
    l2.insertBegining(6)
    l2.insertBegining(7)
    
    
    print(union_intersection_list(ll,l2,perform='i'))
    
    
            
 