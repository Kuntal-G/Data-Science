# Detect Loop in a Linkedlist with Loop Count



class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    
    def __init__(self):
        self.head=None
        
    def push(self,data):
        
        newNode=Node(data)
        
        newNode.next=self.head
        self.head=newNode
        
        return 'Inserted data {} in the begining of list'.format(data)
    
    
        
    def printList(self):
        
        current=self.head
        while (current):
            print(current.data)
            current=current.next
        
    def detectLoop(self):
        
        slow_ptr=self.head
        fast_ptr=self.head
        
        while (slow_ptr and fast_ptr and fast_ptr.next is not None):
            
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next
            if(slow_ptr==fast_ptr):
                
                loop_cnt=self.loopCycleCount(slow_ptr)
                
                return 'Loop found with count {}'.format(loop_cnt)
        
        return 'No loop detected'
    
    
    def loopCycleCount(self,node):
        
        temp=node
        count=1
        while(temp.next is not node):
            
            temp=temp.next
            count+=1
        return count
            


if __name__== '__main__':
    
    ll=LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.printList()
    print(ll.detectLoop())
    ll.head.next.next.next.next = ll.head 

    print(ll.detectLoop())
    
    
            
    
    
    
    

