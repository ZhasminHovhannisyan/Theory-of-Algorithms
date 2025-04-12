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



def redundant(graph):
    """
    Arg:
        graph: graph representation as a dictionary

    Returns:
        remove_edge: list, which contains sublists of edges.
                There is only one redundant edge in the graph, 
                but there might be several ways to reconstruct the graph as a tree.
                Remove one edge at a time, to get different trees   
    """
    start = next(iter(graph)) #get the first key to start
    visited = set()
    queue = [start]
    result = []
    remove_edge = []  # all edges that are possible to remove and get different trees

    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited and neighbour not in queue:
                queue.append(neighbour)
                visited.add(neighbour)
            else:
                remove_edge.append([node, neighbour])
                # check which edge was also entering this neighbour node
                # that edge can also be marked as redundant
                for other_node in graph:
                    if other_node != node and neighbour in graph[other_node]:
                        remove_edge.append([other_node, neighbour])
    return remove_edge


edges1 = [[1,2],[2,3],[3,4],[1,4],[1,5]]
g1 = edgelist_to_dict(edges1)
result_edges1 = redundant(g1)
print(result_edges1)


edges2 = [[1,2],[1,3],[2,3]]
g2 = edgelist_to_dict(edges2)
result_edges2 = redundant(g2)
print(result_edges2)


edges3 = [[1,2],[1,3],[2,4],[2,5],[2,6],[3,7],[3,8],[6,9],[7,9]] 
g3 = edgelist_to_dict(edges3)
result_edges3 = redundant(g3)
print(result_edges3)


