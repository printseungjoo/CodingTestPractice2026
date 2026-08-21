def solution(progresses, speeds):
    answer = []
    daySpents = []
    daySpent = 0
    for i in range(len(progresses)):
        daySpent = (100-progresses[i])//speeds[i]
        if((100-progresses[i])%speeds[i] != 0):
            daySpent+=1
        daySpents.append(daySpent)
        daySpent = 0
    stackNumber = 0
    bigTime = 0
    for j in range(len(daySpents)):
        if(j == 0):
            stackNumber+=1
            bigTime = daySpents[j]
            continue
        if(daySpents[j]>bigTime):
            answer.append(stackNumber)
            stackNumber = 1
            bigTime = daySpents[j]
            continue
        stackNumber+=1
    answer.append(stackNumber)
    return answer