Tree={
    1:[2,7,8],
    2:[3,6],
    3:[4,5],
    4:[],
    5:[],
    6:[],
    7:[],
    8:[9,12],
    9:[10,11],
    12:[],
    10:[],
    11:[]
}
def dfs_recursive(node, visited=None):
    if visited is None:
        visited = set() 
    visited.add(node)
    print(node, end=' ')  

    for neighbor in Tree.get(node, []):
        if neighbor not in visited:
            dfs_recursive(neighbor, visited)
    
    return visited

start_node = 1
print("DFS Traversal Order (Recursive):")
dfs_recursive(start_node)
print() 
