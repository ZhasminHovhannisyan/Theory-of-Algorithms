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


# time complexity of queue.pop(0) is O(n)

# algorithm optimization: use popleft(), time complexity is O(1)

from collections import deque

def bfs_optim(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()  # O(1)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(neighbour for neighbour in graph[node] if neighbour not in visited)


n = 13
graph = {0: [7, 9, 11],
         1: [],
         2: [12],
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

print("BFS starting with your input node:")
print("BFS result: ")
bfs(graph, first_node)

print("/nBFS optimized: ")
bfs_optim(graph, first_node)