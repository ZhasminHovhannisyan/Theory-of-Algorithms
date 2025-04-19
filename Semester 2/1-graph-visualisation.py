import networkx as nx
import matplotlib.pyplot as plt

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

# -------- NetworkX Visualization ----------

def draw_graph_with_components(graph, components):
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = {}
    color_map = {}
    colors = plt.cm.tab20.colors

    # Layout offset per component
    x_offset = 0
    y_offset = 0
    spacing = 5  # space between components

    for i, component in enumerate(components):
        subgraph = G.subgraph(component)
        sub_pos = nx.spring_layout(subgraph, seed=42, k=1.5)  # k increases spacing in component

        # Offset component layout to avoid overlap
        for node in sub_pos:
            sub_pos[node][0] += x_offset
            sub_pos[node][1] += y_offset
            color_map[node] = colors[i % len(colors)]

        pos.update(sub_pos)

        # Shift next component's position
        x_offset += spacing
        if i-1 % 2 == 0:  # move to next row every 2 components
            x_offset = 0
            y_offset -= spacing

    node_colors = [color_map[node] for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors,
            edge_color='gray', node_size=700, font_size=10, width=2)
    plt.title("Connected Components Visualization (Optimized Layout)")
    plt.axis('off')
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
