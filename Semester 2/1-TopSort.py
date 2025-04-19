# topological sort with dfs

def topsort(graph):
    visited = set()
    result = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        result.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return result[::-1]  # reverse to get correct order



# Example graph
mygraph = {
    'A': ['B', 'C', 'D'],
    'B': ['J'],
    'C': ['F', 'I'],
    'D': ['G', 'E'],
    'E': ['K', 'H'],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}

order = topsort(mygraph)
print(order)