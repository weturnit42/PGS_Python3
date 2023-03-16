def solution(board):
    answer = 1
    stretchedBoard = board[0] + board[1] + board[2]

    oCount = stretchedBoard.count('O')
    xCount = stretchedBoard.count('X')

    winCandidate = []
    winCandidate.append([0,3,6])
    winCandidate.append([1,4,7])
    winCandidate.append([2,5,8])
    winCandidate.append([0,1,2])
    winCandidate.append([3,4,5])
    winCandidate.append([6,7,8])
    winCandidate.append([0,4,8])
    winCandidate.append([2,4,6])
    
    if(not(oCount == xCount or oCount-1 == xCount)):
        answer = 0
    
    if(oCount >= 3 and xCount >= 3):
        oIndex = []

        temp = stretchedBoard.find('O')
        oIndex.append(temp)
        while stretchedBoard[temp+1:].find('O') != -1:
            temp = stretchedBoard[temp+1:].find('O') + temp + 1
            oIndex.append(temp)
        
        oWin = False
        for candidate in winCandidate:
            # print(sorted(list(set(oIndex).intersection(candidate))), candidate, list(set(oIndex).intersection(candidate)).sort() == candidate)
            if(sorted(list(set(oIndex).intersection(candidate))) == candidate):
                oWin = True
                break
                
        xIndex = []

        temp = stretchedBoard.find('X')
        xIndex.append(temp)
        while stretchedBoard[temp+1:].find('X') != -1:
            temp = stretchedBoard[temp+1:].find('X') + temp + 1
            xIndex.append(temp)

        xWin = False
        for candidate in winCandidate:
            # print(list(set(xIndex).intersection(candidate)), candidate, list(set(xIndex).intersection(candidate)).sort() == candidate)
            if(sorted(list(set(xIndex).intersection(candidate))) == candidate):
                xWin = True
                break
        # print(oWin, xWin)
        if(oWin == True and xWin == True):
            answer = 0
        elif(oWin == True and xWin == False):
            if(oCount-1 != xCount):
                answer = 0
        elif(xWin == True and oWin == False):
            if(oCount != xCount):
                answer = 0
    return answer