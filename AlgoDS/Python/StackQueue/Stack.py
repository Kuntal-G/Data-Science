#Stack implementation using list

class Stack:

    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0

    def push(self,data):
        self.items.append(data)
        return 'added'

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s=Stack()
print(s.isEmpty())
s.push(3)
s.push(4)
s.push(5)
s.push(4)
print(s.isEmpty())
print(s.peek())
print(s.pop())

