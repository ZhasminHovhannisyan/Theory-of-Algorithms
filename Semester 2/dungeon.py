from collections import deque
def solve(m):

    q = deque()
    q.append((sr, sc, 0))
    visited[sr][sc] = True

    while q:
        r, c, dist = q.popleft()

        if m[r][c] == 'E':
            return dist  # Found the end

        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if rr < 0 or rr >= R or cc < 0 or cc >= C:
                continue
            if visited[rr][cc] or m[rr][cc] == '#':
                continue

            q.append((rr, cc, dist + 1))
            visited[rr][cc] = True

    return -1  # No path to 'E'


matrix = [
    ['S', '', '', '#', '', '', ''],
    ['', '#', '', '', '', '#', ''],
    ['', '#', '', '', '', '', ''],
    ['', '', '#', '#', '', '', ''],
    ['#', '', '#', 'E', '', '#', '']    
]  

R, C = len(matrix), len(matrix[0])
sr, sc = 0, 0 

visited = [[False for _ in range(C)] for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

final_moves = solve(matrix)
print(final_moves)