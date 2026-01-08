from collections import deque
import sys

n,m = map(int, sys.stdin.readline().split())
graph = []
for i in range(m):
    graph.append(list(map(int, sys.stdin.readline().split())))
if(graph[0][0] == 0 or graph[m-1][n-1] == 0):
    print('No')
    sys.exit()
dx = [1, 0]
dy = [0, 1]
q = deque()
q.append((0,0))
graph[0][0] = 2
while q:
    x, y = q.popleft()
    if(x == m-1 and y == n-1):
        break
    for i in range(2):
        nx = x+dx[i]
        ny = y+dy[i]
        if(0<=nx<m and 0<=ny<n and graph[nx][ny]==1):
            graph[nx][ny] = 2
            q.append((nx, ny))
if(graph[m-1][n-1] == 2):
    print('Yes')
else:
    print('No')