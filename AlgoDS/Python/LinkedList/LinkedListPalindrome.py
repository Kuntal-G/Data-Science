# -*- coding: utf-8 -*-

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
    

def checkPalindrome(ll):
    stack=[]
    current=ll.head
    #First loop to insert data
    while(current is not None):
        stack.append(current.data)
        current=current.next
        
    #second pass over the linked list to check palindrome
    current=ll.head
    while(current is not None):
        if current.data != stack.pop():
            return False
        current=current.next
        
    return True

if __name__== '__main__':
    
    ll=LinkedList()
    ll.insertBegining(1)
    ll.insertBegining(2)
    ll.insertBegining(3)
    ll.insertBegining(2)
    ll.insertBegining(1)
    print(checkPalindrome(ll))
    
    
        
    
    

