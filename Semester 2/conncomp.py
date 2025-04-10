
def dfs(graph, at, visited, result):
    
    if visited[at] == True:
        return 
    
    visited[at] = True
    result.append(at)
    for neighbor in graph[at]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, result)
            
    return result



def conncomp(graph):
    visited = {node: False for node in graph}
    components = []
    
    for node in graph:
        if not visited[node]:
            component = []
            dfs(graph, node, visited, component)
            components.append(component)
    
    return components



graph = {
    0: [4, 8, 13, 14],
    1: [5],
    2: [9, 15],
    3: [9],
    4: [0, 8],
    5: [1, 16, 17],
    6: [7, 11],
    7: [6],
    8: [0, 4, 14],
    9: [2, 3, 15],
    10: [15],
    11: [6],
    12: [],
    13: [0, 14],
    14: [0, 13, 8],
    15: [2, 9, 10],
    16: [5],
    17: [5]
}

components_list = conncomp(graph)
print(components_list)