from collections import deque
n,m,k = map(int, input().split())
maps = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    maps[x - 1][y - 1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    cnt = 1
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(n) and ny in range(m) and maps[nx][ny]:
                maps[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

li = []
for i in range(n):
    for j in range(m):
        if maps[i][j]:
            maps[i][j] = 0
            li.append(bfs(i, j))
print(max(li))