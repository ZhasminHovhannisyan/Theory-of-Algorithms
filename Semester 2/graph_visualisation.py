import matplotlib.pyplot as plt
import random

# -------- DFS and Connected Components ----------
def dfs(graph, at, visited, result):
    if visited[at]:
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

# -------- Graph Visualization ----------
def draw_graph_with_components(graph, components):
    plt.figure(figsize=(8, 6))
    nodes = list(graph.keys())
    
    positions = {node: (random.uniform(0, 10), random.uniform(0, 10)) for node in nodes}
    
    colors = plt.cm.tab20.colors
    component_colors = {}
    for i, component in enumerate(components):
        for node in component:
            component_colors[node] = colors[i % len(colors)]

    # Draw edges
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            x_vals = [positions[node][0], positions[neighbor][0]]
            y_vals = [positions[node][1], positions[neighbor][1]]
            plt.plot(x_vals, y_vals, color='gray', zorder=1)

    # Draw nodes with component colors
    for node, (x, y) in positions.items():
        plt.scatter(x, y, color=component_colors[node], s=700, zorder=2)
        plt.text(x, y, str(node), fontsize=10, ha='center', va='center', zorder=3)

    plt.axis('off')
    plt.title('Connected Components Visualization')
    plt.show()

# -------- Main Graph Data --------
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
print("Connected Components:", components_list)
draw_graph_with_components(graph, components_list)
