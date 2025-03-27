############## pseudocode from slides #############
def dfs(graph, at, visited, result):
    
    if visited[at] == True:
        return 
    
    visited[at] = True
    result.append(at)
    for neighbor in graph[at]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, result)
            
    return result




################ with stack ###############

def dfs_iterative(graph, start_node, visited, final_list):
    stack = [start_node]
    
    while stack:
        # print(stack)
        node = stack[-1]
        if not visited[node]:
            #print(node)
            visited[node] = True
            final_list.append(node)
            
            for next in graph[node]:
                if not visited[next]:
                    stack.append(next)
        else:
            stack.pop()
    return final_list






graph = {
    0: [1, 9],
    1: [0, 8],
    2: [],
    3: [2, 5, 4, 7],
    4: [],
    5: [3, 6],
    6: [5, 7],
    7: [3, 6, 10, 11],
    8: [7],
    9: [8],
    10: [11],
    11: [],
    12: [2]
}



node = int(input("enter start node: "))

res = []
visited = [False for _ in range(len(graph))]
path1 = dfs(graph, node, visited, res)
print("first version results: ", path1)

res = []
visited = [False for _ in range(len(graph))]
path2 = dfs_iterative(graph, node, visited, res)
print("second version results: ", path2)
