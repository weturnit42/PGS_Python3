def solution(citations):
    answer = 0
    
    count = [0]*(len(citations)+1)
    for i in range(len(citations)+1):
        cnt = 0
        for j in range(len(citations)):
            if(citations[j] >= i):
                cnt = cnt+1
        # print(cnt)
        if(cnt >= i):
            count[i] = i

    maxCnt = max(count)
    
    return maxCnt