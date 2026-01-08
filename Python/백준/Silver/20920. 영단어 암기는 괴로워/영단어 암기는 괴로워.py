import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
l = []
for i in range(n):
    word = sys.stdin.readline().strip()
    if(len(word)<m):
        continue
    l.append(word)
lCounter = Counter(l)
answer = sorted(lCounter.keys(), key = lambda w:(-lCounter[w], -len(w), w))
print('\n'.join(answer))