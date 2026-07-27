import collections

def solution(k, tangerine):
    answer = 0
    tangerineDict = collections.Counter(tangerine)
    tangerineDict = tangerineDict.most_common()
    for t in tangerineDict:
        k-=t[1]
        answer+=1
        if(k<=0):
            return answer
    return 0