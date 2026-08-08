def solution(s):
    answer = []
    tupleArray = []
    tuplesArray = []
    for i in range(1, len(s)):
        if(s[i] == '{'):
            tupleArray = []
            string = ''
            continue
        if(s[i].isdigit()):
            string+=s[i]
            continue
        if(s[i] == ','):
            tupleArray.append(int(string))
            string = ''
            continue
        tuplesArray.append(tupleArray)
    tuplesArray[-1].append(int(string))
    tuplesArray = tuplesArray[:len(tuplesArray)-1]
    lenSortedTuple = sorted(tuplesArray, key = len)
    for i in range(len(lenSortedTuple)):
        if(i == 0):
            answer.append(lenSortedTuple[i][0])
            continue
        for j in range(len(lenSortedTuple[i])):
            if(lenSortedTuple[i][j] not in answer):
                answer.append(lenSortedTuple[i][j])
                break
    return answer