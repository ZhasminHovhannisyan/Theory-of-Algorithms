def edgelist_to_dict(edge_list):
    graph = {}
    for u, v in edge_list:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u) 
    return graph


def find_path(graph, start, destination):
    
    visited = set()
    
    def dfs(start):
        
        if start == destination:
            return True
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False
    
    return dfs(start)


edges1 = [[0,1],[1,2],[2,0]]
source1 = 0
destination1 = 2
graph1 = edgelist_to_dict(edges1)
answer1 = find_path(graph1, source1, destination1)
print(f"Path {source1} -> {destination1} exists: ", answer1)


edges2 = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source2 = 0
destination2 = 5
graph2 = edgelist_to_dict(edges2)
answer2 = find_path(graph2, source2, destination2)
print(f"Path {source2} -> {destination2} exists: ", answer2)
