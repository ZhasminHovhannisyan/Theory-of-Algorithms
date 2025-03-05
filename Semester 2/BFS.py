n = 13
graph = {0: [7, 9, 11],
         1: [],
         2: [],
         3: [2, 4],
         4: [],
         5: [],
         6: [5],
         7: [6, 3, 11],
         8: [1, 12],
         9: [8, 10, 0],
         10: [1],
         11: [], 
         12: [2]
         }

first_node = int(input("enter the first node: "))



############ version 1 ############

# queue = [first_node]

# for k in queue:
#     for v in graph[k]:
#         if v not in queue:
#             queue.append(v)

# print(queue)

############### version 2 ################
def bfs(graph, start):
    visited = set()  
    queue = [start]  

    while queue:
        node = queue.pop(0)  
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # for neighbour in graph[node]:
            #     if neighbour not in visited:
            #         queue.append(neighbour)
            queue.extend(neighbour for neighbour in graph[node] if neighbour not in visited)


print("BFS starting with your input node:")
bfs(graph, first_node)


############### homework: BFS with pseudocode from slides ##############



