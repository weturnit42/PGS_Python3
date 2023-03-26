from collections import deque

def solution(priorities, location):
    answer = 0
    
    # docs = []
    # for i in range(len(priorities)):
    #     docs.append((i, priorities[i]))
    # docs.reverse()
    # target = docs[len(priorities)-location-1]
    
    # cnt = 0
    # i = len(docs)-1
    # while(len(docs) != 0):
    #     j = i-1
    #     while(j >= 0):
    #         print(i, j, len(docs), docs[i], docs[j])
    #         if(docs[i][1] < docs[j][1]):
    #             temp = docs[i]
    #             del docs[i]
    #             docs.insert(0, temp)
    #             i = i-1
    #         j = j-1
        
    #     print(docs[i])
    #     if(docs[i] == target):
    #         cnt = cnt+1
    #         del docs[i]
    #         i = i+1
    #         return cnt
    #     else:
    #         cnt = cnt+1
    #         del docs[i]
    #         i = i+1
    #     i = i-1

    docs = []
    for i in range(len(priorities)):
        docs.append((i, priorities[i]))
    docs = deque(docs)
    target = docs[location]

    cnt = 0
    i = 0
    while(len(docs) != 0):
        j = i+1
        while(j < len(docs)):
            prior = []
            for k in range(len(docs)):
                prior.append(docs[k][1])
            # print(i, j, len(docs), docs[i], docs[j])
            if(docs[i][1] < max(prior)):
                docs.rotate(-1)
            else:
                break
            j = j+1
        
        # print(docs[i])
        if(docs[0] == target):
            cnt = cnt+1
            docs.popleft()
            # i = i-1
            return cnt
        else:
            cnt = cnt+1
            docs.popleft()
            # i = i-1
        # i = i+1
            
    return answer