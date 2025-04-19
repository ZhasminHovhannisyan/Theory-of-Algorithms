import networkx as nx
import matplotlib.pyplot as plt

def findCenter(edges):
    a, b = edges[0]
    c, d = edges[1]

    if a == c or a == d:
        return a
    else:
        return b


def visualize_graph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=14, edge_color='gray')
    plt.title("Graph Visualization")
    plt.show()


my_edges = [[1,2],[2,3],[4,2]]
visualize_graph(my_edges)
result = findCenter(my_edges)
print(result)

my_edges = [[1,2],[5,1],[1,3],[1,4]]
visualize_graph(my_edges)
result = findCenter(my_edges)
print(result)
