def solution(keymap, targets):
    answer = []
    
    for target in targets:
        tempAnswer = 0
        unableCheck = False
        for i in range(len(target)):
            keyHit = []

            for j in range(len(keymap)):
                keyHit.append(keymap[j].find(target[i]))
            keyHit.sort()

            ans = -1
            for j in range(len(keyHit)):
                if(keyHit[j] == -1):
                    continue
                else:
                    ans = keyHit[j]+1
                    break
            if(ans == -1):
                unableCheck = True
                break
            else:
                tempAnswer = tempAnswer+ans
        if(unableCheck == False):
            answer.append(tempAnswer)
        else:
            answer.append(-1)
    return answer