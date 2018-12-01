#Merge two sorted Linked List

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
    
    
    
    def printList(self):
        
        current=self.head
        while (current):
            print(current.data)
            current=current.next
            
def mergeSortedList(list1,list2):
    
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    
    temp=None
    
    if list1.data <= list2.data:
        temp=list1
        temp.next=mergeSortedList(list1.next,list2)
        
    else:
        temp=list2
        temp.next=mergeSortedList(list1,list2.next)
    
    return temp
        

if __name__== '__main__':
    
    ll=LinkedList()
    ll.insertBegining(4)
    ll.insertBegining(3)
    ll.insertBegining(2)
    ll.insertBegining(1)
    #ll.printList()
    ll2=LinkedList()
    ll2.insertBegining(12)
    ll2.insertBegining(10)
    ll2.insertBegining(7)
    ll2.insertBegining(5)
    #ll2.printList()
    ll3=LinkedList()
    ll3.head=mergeSortedList(ll.head,ll2.head)
    ll3.printList()
    
            
    
    
    
    

