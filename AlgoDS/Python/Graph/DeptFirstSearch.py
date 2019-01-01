#Depth First Search using stack

def depth_first_search(graph,root):
    
    stack=[root]
    visited=set()
    
    while (stack):
        
        vertex=stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            
            stack.extend(graph[vertex]-visited)
            print('stack',stack)
    return visited
   
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(depth_first_search(graph,'A'))