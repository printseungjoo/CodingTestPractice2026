slicedArr = [];

def slicing(s, i):
    global slicedArr;
    s2 = '';
    for j in range(1, len(s)+1):
        s2 += s[j-1];
        if(j%i==0):
            slicedArr.append(s2);
            s2 = '';
    if(len(s2)!=0):
        slicedArr.append(s2);
    return;   

def convert(lenS, slicedArr, i):
    count = 1;
    j = 0;
    tempCount = 0;
    result = lenS;
    while(count != len(slicedArr)):
        if(slicedArr[j] != slicedArr[j+1]):
            if(0<tempCount<9):
                result = result-tempCount*i+1;
            elif(9<=tempCount<99):
                result = result-tempCount*i+2;
            elif(99<=tempCount<999):
                result = result-tempCount*i+3;
            elif(tempCount == 999):
                result = result-tempCount*i+4;
            tempCount = 0;
        else:
            tempCount += 1;
        j += 1;
        count += 1;
    if(tempCount!=0):
        if(0<tempCount<9):
            result = result-tempCount*i+1;
        elif(9<=tempCount<99):
            result = result-tempCount*i+2;
        elif(99<=tempCount<999):
            result = result-tempCount*i+3;
        elif(tempCount == 999):
            result = result-tempCount*i+4;
    return result;
    
def solution(s):
    global slicedArr;
    choiceArr = [];
    
    for i in range(1, len(s)-1):
        slicedArr = [];
        slicing(s, i);
        convertValue = convert(len(s), slicedArr, i);
        choiceArr.append(convertValue);
    choiceArr.append(len(s));
    
    return min(choiceArr);