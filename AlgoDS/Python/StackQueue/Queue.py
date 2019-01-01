#Queue implementation using list

class Queue:

    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0

    def enqueue(self,data):
        self.items.insert(0,data)
        return 'added'

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q=Queue()
print(q.isEmpty())
q.enqueue(3)
q.enqueue(4)
q.enqueue(4)
q.enqueue(5)

print(q.isEmpty())
print(q.dequeue())


