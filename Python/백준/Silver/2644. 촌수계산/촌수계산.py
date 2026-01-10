import sys
from collections import deque

n = int(sys.stdin.readline().strip())
person1, person2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline().strip())
l = [[] for i in range(n+1)]
for i in range(m):
    input1, input2 = map(int, sys.stdin.readline().split())
    l[input1].append(input2)
    l[input2].append(input1)
d = deque()
visited = [-1]*(n+1)
d.append(person1)
visited[person1] = 0
answer = -1
count = 0
while d:
    pL = d.popleft()
    for i in l[pL]:
        if(visited[i] == -1):
            visited[i] = visited[pL]+1
            d.append(i)
print(visited[person2])