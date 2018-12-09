# Circular Linked List

class Link:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class CircularList:
    def __init__(self):
        self.head = Link(None, None) 
        self.head.next = self.head   

    def add(self, data):             
        self.head.next = Link(data, self.head.next)

    def contains(self, data):   
        current = self.head.next
        while current != self.head:
            if current.data == data: 
                return True
            current = current.next
        return False  
    
    def printList(self):
        current=self.head.next
        while current != self.head:
            print(current.data)
            current = current.next
            
        
        
cl=CircularList()
cl.add(1)
cl.add(4)
cl.add(2)
cl.add(5)

print(cl.printList())
print(cl.contains(3))

