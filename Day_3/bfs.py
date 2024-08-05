from collections import deque

Tree={
    'B':['E','X','K'],
    'E':['P','G'],
    'P':['D','T'],
    'D':[],
    'T':[],
    'G':[],
    'X':[],
    'K':['A','R'],
    'A':['H','M'],
    'H':[],
    'M':[],
    'R':[]
}
def bfs(snode):
    visited = set()          
    queue = deque([snode]) 
    result = []             
    while queue:
        node = queue.popleft()  
        if node not in visited:
            visited.add(node)   
            result.append(node) 
            for neighbor in Tree.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return result


root='B'
snode=bfs(root)

print(f"The BFS :",snode)
