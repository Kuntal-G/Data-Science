# LinkedList Intersection

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    
    def __init__(self):
        self.head=None
        
    def insert_beg(self,data):
        
        node=Node(data)
        
        node.next=self.head
        self.head=node
        
    def printList(self):
        
        current=self.head
        while (current):
            print(current.data)
            current=current.next
        
class Test:
        
    def length(self, node):
        
        length=0
        current=node
        while(current is not None):
            current=current.next
            length +=1
        #print(length)
        return length
    
    
    def get_intersection(self,d,node1,node2):
        
        for i in range(d):
            #print(i)
            if node1 is None:
                return -1
            node1=node1.next
            
        while(node1 is not None and node2 is not None):
            print(node1.data,node2.data)
            if node1.data==node2.data:
                return node1.data
            node1=node1.next
            node2=node2.next
            
    def get_node(self,node1,node2):
        
        l1=self.length(node1)
        l2=self.length(node2)
        
        if l1>l2:
            return self.get_intersection(l1-l2,node1,node2)
        else:
            return self.get_intersection(l2-l1,node2,node1)
      
    
                

    
ll=LinkedList()
ll.insert_beg(3)
ll.insert_beg(6)
ll.insert_beg(15)
ll.insert_beg(15)
ll.insert_beg(30)

#print(ll.printList())
    
l2=LinkedList()
l2.insert_beg(10)
l2.insert_beg(12)
l2.insert_beg(40)
l2.insert_beg(15)

#print(l2.printList())

    
t=Test()
    
print(t.get_node(ll.head,l2.head))
           
            

