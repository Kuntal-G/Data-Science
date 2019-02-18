# Validate IP address 

def is_valid_ip(ip):
    
    print('IP check coming:', ip)
    
    ip=ip.split(".")
    
    for i in ip:
        
        if len(i)>3 or int(i)<0 or int(i)>255:
            return False
        elif len(i)>1 and int(i)==0:
            return False
        elif len(i)>1 and int(i)!=0 and i[0]=='0':
            return False
        
    return True

def convert_to_ip(s):
    
    n=len(s)
    
    
    if n>12:
        return []
    
    s_new=s
    
    res=[]
    
    for i in range (1,n-2):
        for j in range(i+1,n-1):
            for k in range (j+1,n):
                
                s_new=s_new[:k]+'.'+s_new[k:]
                
                s_new=s_new[:j]+'.'+s_new[j:]
                
                s_new=s_new[:i]+'.'+s_new[i:]
                
                
                
                if is_valid_ip(s_new):
                    res.append(s_new)
                
                s_new=s
                
    
    return res


A = "25525511135"

print(convert_to_ip(A))
