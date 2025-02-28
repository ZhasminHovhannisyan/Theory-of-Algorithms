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

first_node = int(input("enter your first node: "))
queue = [first_node]
dequeue = []

for k in queue:
    for v in graph[k]:
        if v not in queue:
            queue.append(v)

print(queue)