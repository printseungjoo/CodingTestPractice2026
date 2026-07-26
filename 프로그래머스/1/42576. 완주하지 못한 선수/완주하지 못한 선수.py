def solution(participant, completion):
    participantDict = {}
    for p in participant:
        if p in participantDict:
            participantDict[p]+=1
        else:
            participantDict[p] = 1
    for c in completion:
        participantDict[c]-=1
    for key, value in participantDict.items():
        if(value==1):
            return key
    return ''