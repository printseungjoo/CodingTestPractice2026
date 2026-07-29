def solution(want, number, discount):
    answer = 0
    wantDict = {}
    for i in range(len(want)):
        wantDict[want[i]] = number[i]
    tenValues = []
    for i in range(len(discount)-1):
        tempDict = wantDict
        tenValues = discount[i:i+10]
        indexCount = 0
        for k, v in tempDict.items():
            indexList = [i for i, value in enumerate(tenValues) if value == k]
            if(len(indexList)>=v):
                indexCount+=1
        if(indexCount == len(want)):
            answer+=1
    return answer