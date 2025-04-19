import numpy as np

def setup(m):
    n = len(m)
    dp = np.full((n, n), float('inf'))
    next_matrix = np.full((n, n), -1)
    
    for i in range(n):
        dp[i][i] = 0 
        for j in range(n):
            if m[i][j] != float('inf'):
                dp[i][j] = m[i][j]
                next_matrix[i][j] = j
    
    return dp, next_matrix

def detect_negative_cycle(dp):

    n = len(dp)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (dp[i][k] != float('inf') and 
                    dp[k][j] != float('inf') and 
                    dp[i][k] + dp[k][j] < dp[i][j]):
                    dp[i][j] = float('-inf')
    
    return dp

def floyd_warshall(m):
    m = np.array(m)
    dp, next_matrix = setup(m)
    n = len(m)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):

                if (dp[i][k] != float('inf') and 
                    dp[k][j] != float('inf') and 
                    dp[i][k] + dp[k][j] < dp[i][j]):
                    dp[i][j] = dp[i][k] + dp[k][j]
                    next_matrix[i][j] = next_matrix[i][k]
    
    dp = detect_negative_cycle(dp)
    
    return dp




graph = [
    [0, 4, 1, float('inf')],
    [float('inf'), 0, 6, float('inf')],
    [4, 1, 0, 2],
    [float('inf'), float('inf'), float('inf'), 0]
]

distances = floyd_warshall(graph)

print("All Pairs Shortest Paths:")
print(distances) 