# 특정 원소가 속한 집합을 찾기
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기 (간선 연결한다고 생각!)
def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

class CycleError(Exception): # 사용자 정의 에러
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

# def DFS(stack, visited, finished, parent, node, vertex, edge, isGraphCyclic):
#     # print(node)
#     for v in vertex:
#         if(node != v):
#             print(node, v, visited[v])
#         if((node, v) in edge):
#             if(visited[v] != True):
#                 visited[v] = True
#                 print(node, v, visited[v], "frontEdge")
#                 parent[v] = node
#                 DFS(stack, visited, finished, parent, v, vertex, edge, isGraphCyclic)
                
#         elif((v, node) in edge):
#             if(visited[node] != True):
#                 visited[node] = True
#                 print(node, v, visited[v], "backEdge")
#                 parent[node] = v
#                 DFS(stack, visited, finished, parent, node, vertex, edge, isGraphCyclic)

#     finished[v] = True

# def denoteCycle(node, v, cycleList):
#     cycleList.append(v)

#     if(parent[v] in cycleList):
#         return

#     denoteCycle(node, parent[v], cycleList)

# def DFS(edge, v, visited, parent, trace):
#     visited[v] = True
#     trace.append(v)

#     for e in edge:
#         if e[0] == v:            
#             if not visited[e[1]]:            
#                 parent[e[1]] = v
#                 print(v, e[1])
#                 DFS(edge, e[1], visited, parent, trace) 

#                 nonDirectParent = []
#                 for i in range(len(visited)):
#                     if((i, e[1]) in edge and parent[e[1]] != i):
#                         nonDirectParent.append(i)
#                 # print(e[1], 'nonDirectParent', nonDirectParent)

#                 for i in range(len(nonDirectParent)):
#                     if(nonDirectParent[i] in trace):
#                         print(e[1], nonDirectParent[i], "check")

#                         cycle = trace[trace.index(nonDirectParent[i]):]

#                         print(e[1], 'nonDirectParent', nonDirectParent, 'trace', trace, 'cycle', cycle)
#                         raise CycleError("cycle")
                        
#         elif e[1] == v:
#             if not visited[e[0]]:
#                 parent[e[0]] = v
#                 print(v, e[0], "reverse")
#                 DFS(edge, e[0], visited, parent, trace) 

#                 nonDirectParent = []
#                 for i in range(len(visited)):
#                     if((e[0], i) in edge and parent[e[0]] != i):
#                         nonDirectParent.append(i)
#                 # print(e[1], 'nonDirectParent', nonDirectParent)

#                 for i in range(len(nonDirectParent)):
#                     if(nonDirectParent[i] in trace):
#                         print(nonDirectParent[i], e[0], "reverse check")

#                         cycle = trace[trace.index(nonDirectParent[i]):]

#                         print(e[0], 'nonDirectParent', nonDirectParent, 'trace', trace, 'cycle', cycle)
#                         raise CycleError("cycle")

# v = 7
# e = 9
# parent = [-1] * v
# edge = []
# edge.append((0,1,1))
# edge.append((0,5,1))
# # edge.append((0,6,1))
# edge.append((1,2,1))
# edge.append((1,5,1))
# edge.append((2,3,1))
# edge.append((3,5,1))
# edge.append((3,6,1))
# edge.append((4,5,1))
# edge.append((5,6,1))

v = 4
vertex = []
for i in range(v):
    vertex.append(i)
# e = 6
parent = [-1] * v
edge = []
edge.append((0,1))
edge.append((0,2))
edge.append((0,3))
edge.append((1,2))
edge.append((1,3))
edge.append((2,3))

# v = 5
# vertex = []
# for i in range(v):
#     vertex.append(i)
# edge = []
# edge.append((0,1))
# edge.append((0,3))
# edge.append((1,2))
# edge.append((1,3))
# edge.append((1,4))
# edge.append((2,4))

# cycle = False
# cycleCount = 0

# for i in range(v):
#     print(i, "==============")
#     for j in range(0, v):
#         parent[j] = j
#     temp = []
#     for j in range(len(edge)):
        
#         a = edge[(j+i)%v][0]
#         b = edge[(j+i)%v][1]

#         if(find(parent, a) == find(parent, b)):
#             cycle = True
#             cycleCount = cycleCount+1
#             # temp.append(parent)
#             temp.append(a)
#             temp.append(b)
#             print(temp)
#             print("----------------------")
#             # break
#         else:
#             union(parent, a, b)
#             temp.append(a)
#             temp.append(b)

# for i in range(len(edge)):
#     stack = []
#     newEdge = []
#     visited = [False]*v
#     for j in range(len(edge)):
#         newEdge.append(edge[(i+j)%len(edge)])
#     try:
#         print(newEdge)
#         DFS(stack, visited, 0, list(range(v)), newEdge)
#         print("-----------------")
#     except CycleError:
#         print(stack)
#         print("-----------------")

for i in range(v):
    newVertex = []
    for j in range(v):
        newVertex.append((i+j)%v)
    for j in range(len(edge)):
        newEdge = []
        for k in range(len(edge)):
            newEdge.append(edge[(j+k)%len(edge)])
        stack = []
        visited = [False]*v
        finished = [False]*v
        parent = []
        for k in range(v):
            parent.append(k)
        parent[i] = -1
        isGraphCyclic = False
        trace = []
        # for j in range(v):
        #     trace.append(j)

        print(i, newVertex)
        print(newEdge)
        try:
            DFS(newEdge, i, visited, parent, trace)
        except CycleError:
            print("cycle")
        # print(parent)
        # print(trace)
        print("-----------------")

# print(cycle)
# print(cycleCount)