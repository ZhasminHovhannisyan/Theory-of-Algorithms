def topsort(graph):
    visited = set()
    result = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor, _ in graph[node]:
            dfs(neighbor)
        result.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return result[::-1]


def DAG_longest_path(graph, start):
    
    neg_graph = {u: [(v, -w) for v, w in edges] for u, edges in graph.items()}
    top_order = topsort(neg_graph)
    dist = {node: float('inf') for node in neg_graph}
    dist[start] = 0

    for u in top_order:
        if dist[u] != float('inf'):
            for v, neg_weight in neg_graph[u]:
                if dist[u] + neg_weight < dist[v]:
                    dist[v] = dist[u] + neg_weight

    for node in dist:
        if dist[node] != float('inf'):
            dist[node] = -dist[node]
        else:
            dist[node] = float('-inf')  # unreachable

    return dist


g = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: []
}

result = DAG_longest_path(g, 0)
print(result)
