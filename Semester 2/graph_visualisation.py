import matplotlib.pyplot as plt
import random

def create_graph():
    edges = input("Enter the connections in this format A-B, B-C, etc: ").split(',')
    node_pairs = [] 
    nodes = set()
    
    for edge in edges:
        pairs = edge.strip().split('-')
        node_pairs.append(pairs)
        nodes.update(pairs)
    
    return node_pairs, list(nodes)

def draw_graph(graph, nodes):
    plt.figure(figsize=(5, 4))
    
    # Generate random positions for nodes
    positions = {node: (random.uniform(0, 10), random.uniform(0, 10)) for node in nodes}
    
    for edge in graph:
        x_values = [positions[edge[0]][0], positions[edge[1]][0]]
        y_values = [positions[edge[0]][1], positions[edge[1]][1]]
        plt.plot(x_values, y_values, 'gray')
    
    # Draw nodes
    for node, (x, y) in positions.items():
        plt.scatter(x, y, color='lightblue', s=700)
        plt.text(x, y, node, fontsize=10, ha='center', va='center')
    
    plt.axis('off') 
    plt.show()  

graph, nodes = create_graph()  
draw_graph(graph, nodes)

