import sys
from collections import deque

n = int(sys.stdin.readline().strip())
l = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1, n2 = map(int, sys.stdin.readline().split())
    l[n1].append(n2)
    l[n2].append(n1)
d = deque()
visited = [-1 for _ in range(n+1)]
answer = [0 for _ in range(n+1)]
d.append(1)
visited[1] = visited[1]+1
while d:
    d_pop = d.popleft()
    for i in l[d_pop]:
        if visited[i] == -1:
            d.append(i)
            visited[i] = visited[i]+1
            answer[i] = d_pop
for i in range(2, n+1):
    print(answer[i], end='\n')