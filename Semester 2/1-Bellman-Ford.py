def BellmanFord(graph, source):
    v = len(graph)
    edges = []
    for at in graph:
        for to, weight in graph[at]:
            edges.append((at, to, weight))
    
    distance = [float('inf') for _ in range(v)]
    distance[source] = 0
    
    # Relax v-1 times
    for _ in range(v-1):
        for at, to, weight in edges:
            if distance[at] != float('inf') and distance[at] + weight < distance[to]:
                distance[to] = distance[at] + weight
    
    # detect negative cycle
    changed = False
    for at, to, weight in edges:
        if distance[at] != float('inf') and distance[at] + weight < distance[to]:
            distance[to] = float('-inf')
            changed = True
    
    # set distance to all nodes after negative cycle to -inf 
    if changed:
        for _ in range(v - 1):
            for at, to, weight in edges:
                if distance[at] == float('-inf') and distance[to] != float('-inf'):
                    distance[to] = float('-inf')
        return "Graph contains a negative cycle", distance
    
    return distance


g = {
    0: [(1, 5)],
    1: [(6, 60), (5, 30), (2, 20)],
    2: [(3, 10), (4, 75)],
    3: [(2, -15)],
    4: [(9, 100)],
    5: [(6, 5), (8, 50)],
    6: [(7, -50)],
    7: [(8, -10)],
    8: [],
    9: []
}

src = 0
result = BellmanFord(g, src)
print(result)