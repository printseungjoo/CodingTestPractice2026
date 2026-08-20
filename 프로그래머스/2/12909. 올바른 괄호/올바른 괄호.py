def solution(s):
    answer = False
    stackNumber = 0
    for i in range(len(s)):
        if(stackNumber == -1):
            answer = False
            break
        if(s[i] == '('):
            stackNumber+=1
        if(s[i] == ')'):
            stackNumber-=1
    if(stackNumber == 0):
        answer = True
    return answer