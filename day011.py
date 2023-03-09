def solution(numbers):
    answer = []
    
    for n in numbers:
        binaryN = bin(n)
        stringTempN = str(binaryN).replace('0b', '')
        stringN = []
        
        tempPower = 1
        while(pow(2, tempPower) <= n):
            tempPower = tempPower+1
        
        power = 1
        while(pow(2, power) < 2*tempPower):
            power = power+1
        power = power-1
        
        for i in range(pow(2, power)-1):
            if(i < len(stringTempN) and stringTempN[i] == '1'):
                stringN.append(1)
            elif(i < len(stringTempN) and stringTempN[i] == '0'):
                stringN.append(0)
            elif(i >= len(stringTempN)):
                stringN.insert(0, 0)
        
        levelOrderStringN = []
        
        # for i in range(len(stringN)):
        for i in range(power-1, -1, -1):
            for j in range(pow(2, power-1-i)):
                levelOrderStringN.append(stringN[pow(2,i)+j*pow(2, i+1)-1])
#             2 1 0 8 3
#             1 2 1 4 2
#             0 4 2 2 1
        # print(tempPower, power, stringN, levelOrderStringN)
        
        ans=1
        for i in range(1, len(levelOrderStringN)):
            if(i % 2 == 0):
                if(levelOrderStringN[i] == 1 and levelOrderStringN[(i//2)-1] == 0):
                    ans=0
                    break
            else:
                if(levelOrderStringN[i] == 1 and levelOrderStringN[(i-1)//2] == 0):
                    ans=0
                    break
        answer.append(ans)
        '''
             0
           1   2
          3 4 5 6
        
        '''
        
    return answer