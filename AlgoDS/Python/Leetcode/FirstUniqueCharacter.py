#First non-repeating character in  string

def first_unique(s):
    
    letters='abcdefghijklmnopqrstuvwxyz'
    
    index=[s.index(l) for l in letters if s.count(l)==1]
    
    return min(index) if len(index)>0 else -1

s='aefefrtdta'
print(first_unique(s))


