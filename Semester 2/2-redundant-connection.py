import matplotlib.pyplot as plt
import networkx as nx
def edgelist_to_dict(edge_list):
    """
    Arg:
        edge_list: edge list as given in leetcode examples

    Returns:
        dictionary: keys are the nodes
                    values are the outgoing nodes from the key node, kept as list of integers
    """
    graph = {}
    for sublist in edge_list:
        if sublist[0] not in graph:
            graph[sublist[0]] = []
        graph[sublist[0]].append(sublist[1])
        if sublist[1] not in graph:
            graph[sublist[1]] = []
    return graph


def redundant_edges(graph):
    """
    Finds all cycles in the graph using BFS.

    Args:
        graph: dictionary representation of the graph

    Returns:
        List of all unique edges that are part of any cycle.
    """
    visited = set()
    cycles = set()  # Store edges in cycles as frozensets of sorted tuples

    for start_node in graph:
        if start_node in visited:
            continue

        queue = [start_node]
        parent = {start_node: None}
        visited_local = set([start_node])

        while queue:
            node = queue.pop(0)

            for neighbor in graph[node]:
                if neighbor in visited_local and neighbor != parent[node]:
                    # Detected a cycle
                    path1 = []
                    current = node
                    while current is not None:
                        path1.append(current)
                        current = parent[current]

                    path2 = []
                    current = neighbor
                    while current is not None:
                        path2.append(current)
                        if current in path1:
                            common_idx = path1.index(current)
                            cycle = path1[:common_idx + 1] + path2[:-1]
                            for i in range(len(cycle) - 1):
                                edge = tuple(sorted((cycle[i], cycle[i + 1])))
                                cycles.add(frozenset(edge))
                            # Closing edge
                            edge = tuple(sorted((cycle[-1], cycle[0])))
                            cycles.add(frozenset(edge))
                            break
                        current = parent[current]

                if neighbor not in visited_local:
                    parent[neighbor] = node
                    visited_local.add(neighbor)
                    queue.append(neighbor)

        visited.update(visited_local)

    # Convert back to list of edges
    result = [list(edge) for edge in {tuple(e) for c in cycles for e in [tuple(c)]}]
    return result

def visualize_cycle_graph(edges, cycle_edges):
    G = nx.Graph()
    G.add_edges_from(edges)

    edge_colors = []
    for edge in G.edges():
        # Handle both directions
        if list(edge) in cycle_edges or list(reversed(edge)) in cycle_edges:
            edge_colors.append('red')
        else:
            edge_colors.append('gray')

    pos = nx.spring_layout(G, seed=42)  # For consistent layout
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=700, font_size=14, edge_color=edge_colors, width=2.5)

    plt.title("Graph with Cycle Highlighted (Red Edges)")
    plt.show()


edges1 = [[1,2],[2,3],[3,4],[1,4],[1,5]]
g1 = edgelist_to_dict(edges1)
result_edges1 = redundant_edges(g1)
print(result_edges1)

edges2 = [[1,2],[1,3],[2,3]]
g2 = edgelist_to_dict(edges2)
result_edges2 = redundant_edges(g2)
print(result_edges2)

edges3 = [[1,2],[1,3],[2,4],[2,5],[2,6],[3,7],[3,8],[6,9],[7,9]]
g3 = edgelist_to_dict(edges3)
result_edges3 = redundant_edges(g3)
print(result_edges3)

visualize_cycle_graph(edges1, result_edges1)
visualize_cycle_graph(edges2, result_edges2)
visualize_cycle_graph(edges3, result_edges3)
