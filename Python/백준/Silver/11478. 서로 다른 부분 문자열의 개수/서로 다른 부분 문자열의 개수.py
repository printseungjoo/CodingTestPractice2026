import sys

S = list(sys.stdin.readline().strip())
l = list()
for i in range(0, len(S)):
    for j in range(1, len(S)+1):
        if(i>=j):
            continue
        l.append(''.join(S[i:j]))
print(len(set(l)))