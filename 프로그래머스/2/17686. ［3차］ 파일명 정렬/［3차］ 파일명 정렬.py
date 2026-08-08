def solution(files):
    answer = []
    sortedArray = []
    for i in range(len(files)):
        head = ''
        number = 0
        digit = False
        digitStart = 0
        original = files[i]
        visited = False
        ohn = []
        for j in range(len(files[i])):
            if(files[i][j].isdigit() and digit == False):
                head = files[i][:j]
                digitStart = j
                digit = True
            if(digit == True):
                if not files[i][j].isdigit():
                    visited = True
                    number = files[i][digitStart:j]
                    break
        if(visited == False):
            number = files[i][digitStart:]
        ohn.append(original)
        ohn.append(head.lower())
        ohn.append(int(number))
        sortedArray.append(ohn)
    finalSortedArray = sorted(sortedArray, key = lambda x:(x[1], x[2]))
    for i in range(len(finalSortedArray)):
        answer.append(finalSortedArray[i][0])
    return answer