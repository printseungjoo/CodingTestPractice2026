from collections import deque

def solution(cards1, cards2, goal):
    answer = 'Yes'
    d1 = deque()
    d2 = deque()
    for i in cards1:
        d1.append(i)
    for j in cards2:
        d2.append(j)
    for i in goal:
        if(len(d1)!=0 and d1[0] == i):
            d1.popleft()
        elif(len(d2)!=0 and d2[0] == i):
            d2.popleft()
        else:
            answer = 'No'
    return answer