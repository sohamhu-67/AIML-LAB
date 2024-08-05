from collections import deque

# Define the tree as a dictionary
tree = {
    'B': ['E', 'X', 'K'],
    'E': ['P', 'G'],
    'P': ['D', 'T'],
    'D': [],
    'T': [],
    'G': [],
    'X': [],
    'K': ['A', 'R'],
    'A': ['H', 'M'],
    'H': [],
    'M': [],
    'R': []
}

def bfs(start_node):
    visited = set()          
    queue = deque([start_node]) 
    result = []             

    while queue:
        node = queue.popleft()  
        if node not in visited:
            visited.add(node)   
            result.append(node) 
            for neighbor in tree.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return result

# Example usage:
start_node = 'B'
bfs_result = bfs(start_node)
print("BFS Traversal Order:", bfs_result)
