# Bread First Search using DeQueue

from collections import deque

def breadth_first_search(graph,root):
    
    queue=deque([root])
    visited=set([root])
    
    while (len(queue)>0):
        
        vertex=queue.popleft()
        
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited


def breadth_first_search2(graph,root):
    
    queue=[root]
    visited=set()
    
    while (queue):
        
        vertex=queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]-visited)
    return visited
    

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


print(breadth_first_search(graph,'A'))
print(breadth_first_search2(graph,'A'))
