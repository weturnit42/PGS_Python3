import heapq

def solution(n, edge):
    answer = 0
    
#     dist = [[9999999]*n for i in range(n)]
    
#     for i in range(n):
#         for j in range(n):
#             if(i==j):
#                 dist[i][j] = 0
#             elif([i+1,j+1] in edge or [j+1, i+1] in edge):
#                 dist[i][j] = 1
    
#     for i in range(n):
#         for j in range(n):
#             if(dist[0][j]+dist[j][i] < dist[0][i]):
#                 dist[0][i] = dist[0][j]+dist[j][i]
    
#     for i in range(len(dist[0])):
#         if(dist[0][i] == 9999999):
#             dist[0][i] = -1
#     maxDist = max(dist[0])
    
#     for i in range(len(dist[0])):
#         if(dist[0][i] == maxDist):
#             answer = answer+1

#     edgeMatrix = [[9999999]*n for i in range(n)]
    #     dist = [99999999]*n
    #     dist[0] = 0
    #     visited = [False]*n
    #     visited[0] = True
        
    #     for i in range(n):
    #         edgeMatrix[i][i] = 0
        
    #     for _edge in edge:
    #         edgeMatrix[_edge[0]-1][_edge[1]-1] = 1
    #         edgeMatrix[_edge[1]-1][_edge[0]-1] = 1
    #     # print(edgeMatrix)
    #     for i in range(n):
    #         whereToGo = 0
    #         minDist = 99999999
            
    #         for j in range(1,n):
    #             if dist[j] < minDist and not visited[j]:
    #                 minDist = dist[j]
    #                 whereToGo = j
    #         visited[whereToGo] = True
    #         # print("whereToGo", whereToGo)
    #         for j in range(len(edgeMatrix[whereToGo])):
    #             # print(j)
    #             cost = dist[whereToGo] + edgeMatrix[whereToGo][j]
                
    #             if cost < dist[j]:
    #                 dist[j] = cost

#     # print(dist)
    
#     edgeMatrix = [[9999999]*n for i in range(n)]
#     dist = [99999999]*n
#     dist[0] = 0
#     visited = [False]*n
#     visited[0] = True
    
#     for i in range(n):
#         edgeMatrix[i][i] = 0
    
#     for _edge in edge:
#         edgeMatrix[_edge[0]-1][_edge[1]-1] = 1
#         edgeMatrix[_edge[1]-1][_edge[0]-1] = 1
    
#     q = []
#     heapq.heappush(q,(0,0))
#     dist[0]=0

#     while q:
#         _dist, whereToGo = heapq.heappop(q)
#         if dist[whereToGo] < _dist:
#             continue
#         for i in range(len(edgeMatrix[whereToGo])):
#             cost = _dist + edgeMatrix[whereToGo][i]
#             if cost < dist[i]:
#                 dist[i]=cost
#                 heapq.heappush(q,(cost,i))
    
#     for i in range(len(dist)):
#         if(dist[i] == 9999999):
#             dist[i] = -1
#     maxDist = max(dist)
    
#     for i in range(len(dist)):
#         if(dist[i] == maxDist):
#             answer = answer+1

    edge.sort()
    adjList = [[] for i in range(n)]
    dist = [99999999]*n
    dist[0] = 0
    visited = [False]*n
    visited[0] = True
    
    for _edge in edge:
        adjList[_edge[0]-1].append(_edge[1]-1)
        adjList[_edge[1]-1].append(_edge[0]-1)
        
    q = []
    heapq.heappush(q,(0,0))
    dist[0]=0

    while q:
        _dist, whereToGo = heapq.heappop(q)
        if dist[whereToGo] < _dist:
            continue
        for v in adjList[whereToGo]:
            cost = _dist + 1
            if cost < dist[v]:
                dist[v]=cost
                heapq.heappush(q,(cost,v))

    for i in range(len(dist)):
        if(dist[i] == 9999999):
            dist[i] = -1
    maxDist = max(dist)

    for i in range(len(dist)):
        if(dist[i] == maxDist):
            answer = answer+1
    
    return answer