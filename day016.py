def solution(numbers):
    answer = []
    
    # for i in range(len(numbers)):
    #     for j in range(i, len(numbers)):
    #         if(numbers[i] < numbers[j]):
    #             answer.append(numbers[j])
    #             break
    #         if(j == len(numbers)-1):
    #             answer.append(-1)
    #             break
    
#     3 2 1 4
    
    # answer = [-1]*len(numbers)
    
    # for i in range(len(numbers)-2,-1,-1):
        # for j in range(i, len(numbers)):
        #     if(numbers[i] < numbers[j]):
        #         answer[i] = numbers[j]
        #         break
        #     for k in range(j, len(numbers)):
        #         if(numbers[i] < answer[k]):
        #             answer[i] = answer[k]
        #             break
        
#         if(numbers[i] < numbers[i+1]):
#             answer[i] = numbers[i+1] 
#         elif(numbers[i] < answer[i+1]):
#             answer[i] = answer[i+1]
#         else:
#             for j in range(i+2, len(numbers)):
#                 if(numbers[i] < answer[j]):
#                     answer[i] = answer[j]
#                     break 

#     answer = [-1]*len(numbers)

#     for i in range(len(numbers)-2,-1,-1):
#         if(numbers[i] < numbers[i+1]):
#             answer[i] = numbers[i+1] 
#         else:
#             sortedNumbers = sorted(list(enumerate(numbers[len(numbers):i:-1])), key = lambda x:x[1])
#             temp = len(numbers)-1
            
#             for idx, num in sortedNumbers:
#                 if(idx < temp and num > numbers[i]):
#                     temp = idx
#                     answer[i] = num

    answer = [-1]*len(numbers)
#     10  5  2 7  8  11  1  7
#     11  7  7 8 11  -1  7 -1

#     30   25  20   50   10   40
#     50   50  50   -1   40   -1
    stack = []
    for i in range(len(numbers)-1,-1,-1):
        while(len(stack) != 0 and numbers[i] >= stack[-1]):
            answer[i] = stack.pop()
        if(len(stack) == 0):
            answer[i] = -1
        else:
            answer[i] = stack[-1]
            
        stack.append(numbers[i])
                
        # if(numbers[i] < numbers[i+1]):
        #     answer[i] = numbers[i+1]
        #     stack.append(answer[i])
        # else:
        #     while(len(stack) != 0 and numbers[i] < stack[-1]):
        #         answer[i] = stack.pop()
                
        # if(numbers[i] < numbers[i+1]):
        #     answer[i] = numbers[i+1]
        # elif(numbers[i] > max(numbers[i+1:])):
        #     answer[i] = -1
        # else:
        #     if(numbers[i] == max(numbers)):
        #         answer[i] = -1
        #         break
        #     answer[i] = answer[i+1]
        
#         if(numbers[i] < numbers[i+1]):
#             answer[i] = numbers[i+1]
#             stack.append(answer[i])
#         elif(numbers[i] >= max(numbers[i+1:])):
#             answer[i] = -1
#         else:
#             answer[i] = stack.pop()
                    
    return answer