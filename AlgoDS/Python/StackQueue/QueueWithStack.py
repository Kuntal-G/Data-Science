# Queue using Stack

class Queue:
    
    def __init__(self):
        self.inbox=Stack()
        self.outbox=Stack()
        
        
    def enqueue(self,data):
        self.inbox.push(data)
        return "Data inserted into Queue"
        
        
    def dequeue_costly(self):
        if self.outbox.is_empty():
            while(not self.inbox.is_empty()):
                self.outbox.push(self.inbox.pop())
        return self.outbox.pop()
        
    
        
        
class Stack:
    
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return self.items==[]
    
    def push(self,data):
        self.items.append(data)
        return "{} inserted".format(data)
    
    def pop(self):
        return self.items.pop()
    
queue=Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue_costly())

