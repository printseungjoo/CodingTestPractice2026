def solution(clothes):
    answer = 1
    clothesDict = {}
    for nameType in clothes:
        if nameType[1] not in clothesDict:
            clothesDict[nameType[1]] = []
        clothesDict[nameType[1]].append(nameType[0])
    if(len(clothesDict)==1):
        for k, v in clothesDict.items():
            return(len(v))
    for k, v in clothesDict.items():
        answer*=(len(v)+1)
    return answer-1