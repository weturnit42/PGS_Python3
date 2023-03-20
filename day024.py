def solution(n, results):
    answer = 0
    
    # adjList = [[] for i in range(n)]
    winDist = [[9999999] * n for i in range(n)]
#     loseDist = [[9999999] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if(i==j):
                winDist[i][j] = 0
            elif([i+1,j+1] in results):
                winDist[i][j] = 1
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(winDist[i][k]+winDist[k][j] < winDist[i][j]):
                    winDist[i][j] = winDist[i][k]+winDist[k][j]
    
    answer = n
    for i in range(n):
        for j in range(n):
            if(min(winDist[i][j], winDist[j][i]) == 9999999):
                answer = answer-1
                break
                
#     # for i in range(n):
#     #     check = True
#     #     for j in range(n):
#     #         if(min(dist[i][j], dist[j][i]) == 9999999):
#     #             check = False
#     #     if(check == True):
#     #         answer = answer+1

#     # answers=[0 for _ in range(n)]
#     # for i in range(0, n):
#     #     for j in range(0, n):
#     #         if i!=j and winDist[i][j]!=9999999:
#     #             answers[i]+=1
#     #             answers[j]+=1
#     # for i in range(0, n):
#     #     if answers[i]==n-1:
#     #         answer+=1
    
    return answer