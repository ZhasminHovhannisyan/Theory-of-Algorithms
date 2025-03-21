def lazy_dijkstra(graph, first_node, last_node):
    distance = [float('inf') for _ in graph]
    distance[first_node] = 0
    priority_queue = [(first_node, 0)]
    while priority_queue:
        # find the node with the smallest distance in priority queue
        index = 0
        for i in range(1, len(priority_queue)):
            if priority_queue[i][1] < priority_queue[index][1]:
                index = i
        
        # remove the node with smallest distance
        current_dist, current_node = priority_queue.pop(index)
        
        if current_node == last_node:
            return current_dist
        
        if current_dist > distance[current_node]:
            continue
        
        for neighbour, weight in graph[current_node]:
            dist = current_dist + weight    
            
            if dist < distance[neighbour]:
                distance[neighbour] = dist
                priority_queue.append((dist, neighbour))
      
    
          
g = {
    0: [(1,4), (2,1)],
    1: [(3,1)],
    2: [(1,2), (3,5)],
    3: [(4,3)],
    4: []
}

start = int(input("enter the first node: "))
finish = int(input("enter the last node: "))


dist = lazy_dijkstra(g, start, finish)
print(dist)