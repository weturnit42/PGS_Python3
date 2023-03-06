# def solution(n, m, section):
#     answer = 0
    
#     wall = []
#     for i in range(n):
#         wall.append(1)
#     for i in range(len(section)):
#         wall[section[i]-1] = 0
        
#     while(wall[section[-1]-1] == 0):
#         target = min(section)-1
        
#         for i in range(target, target+m):
#             if(i >= len(wall)):
#                 break
#             wall[i] = 1
        
#         answer = answer + 1
#     return answer

def solution(n, m, section):
    answer = 0
    
    wall = []
    for i in range(n):
        wall.append(1)
    for i in range(len(section)):
        wall[section[i]-1] = 0
        
    while(len(section) != 0):
        target = section[0]-1
        
        for i in range(target, target+m):
            if(i >= len(wall)):
                break
            if(wall[i] == 0):
                section.remove(i+1)
                wall[i] = 1
            
        
#         if(len(section) != 1):
#             del section[0]
            
        answer = answer + 1
    return answer