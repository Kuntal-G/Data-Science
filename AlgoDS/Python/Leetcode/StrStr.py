#Implement strstr function similar to find

def str_str(haystack,needle):
    
    index=0
    
    while index<=len(haystack)-len(needle)+1:
        
        if haystack[index:index+len(needle)]==needle:
            
            return index
        index+=1
    
    return -1

print(str_str("GeeksforGeeks","for"))