import matplotlib.pyplot as plt
import networkx as nx

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

def dfs_cycle_detect(node, parent, graph, visited, path, cycles):
    visited.add(node)
    path[node] = parent

    for neighbor in graph[node]:
        if neighbor == parent:
            continue
        if neighbor in visited:
            # Found a cycle
            cycle = []
            x = node
            while x != neighbor and x is not None:
                cycle.append((x, path[x]))
                x = path[x]
            cycle.append((neighbor, node))
            for u, v in cycle:
                if u is not None and v is not None:
                    edge = tuple(sorted((u, v)))
                    cycles.add(frozenset(edge))

        else:
            dfs_cycle_detect(neighbor, node, graph, visited, path, cycles)

def find_cycle_edges_dfs(graph):
    visited = set()
    cycles = set()
    for node in graph:
        if node not in visited:
            dfs_cycle_detect(node, None, graph, visited, {}, cycles)
    return [list(edge) for edge in {tuple(e) for c in cycles for e in [tuple(c)]}]

def visualize_cycle_graph(edges, cycle_edges):
    G = nx.Graph()
    G.add_edges_from(edges)

    edge_colors = []
    for edge in G.edges():
        if list(edge) in cycle_edges or list(reversed(edge)) in cycle_edges:
            edge_colors.append('red')
        else:
            edge_colors.append('gray')

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=700, font_size=14, edge_color=edge_colors, width=2.5)

    plt.title("Graph with Cycle Highlighted (Red Edges)")
    plt.show()

edges3 = [[1,2],[1,3],[2,4],[2,5],[2,6],[3,7],[3,8],[6,9],[7,9]]
g3 = edgelist_to_dict(edges3)
cycle_edges = find_cycle_edges_dfs(g3)
print("Cycle edges:", cycle_edges)
visualize_cycle_graph(edges3, cycle_edges)
