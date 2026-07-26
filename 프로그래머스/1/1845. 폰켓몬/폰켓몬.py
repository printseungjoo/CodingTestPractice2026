def solution(nums):
    answer = 0
    numsSet = set(nums);
    pickNum = len(nums)//2;
    if(pickNum<=len(numsSet)):
        answer = pickNum;
    else:
        answer = len(numsSet);
    return answer