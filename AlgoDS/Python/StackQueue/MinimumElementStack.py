# Minimum Element from the Stack

class Stack:
    
    def __init__(self):
        self.data=[]
        self.minData=[]
        
    def push(self,newData):
        self.data.append(newData)
        
        if len(self.minData)==0 or newData<= self.minData[-1]:
            self.minData.append(newData)
    
    def pop(self):
        
        if len(self.data)==0:
            return None
        else:
            if self.data[-1]==self.minData[-1]:
                self.minData.pop()
            return self.data.pop()
        
    def top(self):
        if len(self.data)==0: 
            return None
        else:
            return self.data[-1]
    
    def get_min(self):
        
        if len(self.minData)==0: 
            return None
        else:
            return self.minData[-1]
        
arr=[2,1,4,8,9,6,7]
s=Stack()

for i in arr:
    s.push(i)
print(s.pop())
print(s.get_min())    

        
        
        
            
    

