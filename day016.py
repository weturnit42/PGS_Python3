# def solution(numbers):
#     answer = []
    
#     # for i in range(len(numbers)):
#     #     for j in range(i, len(numbers)):
#     #         if(numbers[i] < numbers[j]):
#     #             answer.append(numbers[j])
#     #             break
#     #         if(j == len(numbers)-1):
#     #             answer.append(-1)
#     #             break
    
#     answer = [-1]*len(numbers)
    
#     for i in range(len(numbers)-1,0,-1):
#         tempI = numbers[i]
#         temp = numbers[i]
#         for j in range(i,len(numbers)):
#             # print(numJ, numbers[i])
            
#             if(temp < numbers[j]):
#                 temp = numbers[j]
#                 answer[i] = numbers[j]
                
#             if(numbers[j] > numbers[i]):
#                 answer[i] = numbers[j]
#                 break
                
#     return answer

def solution(numbers):
    answer = [-1]*len(numbers)
    
    # for i in range(len(numbers)-2,-1,-1):
    #     if(numbers[i] < numbers[i+1]):
    #         answer[i] = numbers[i+1] 
    #     else:
    #         tempAnswer = list(answer[i:])
    #         ans = tempAnswer[0]
    #         while(len(tempAnswer) != 0 and numbers[i] >= ans):
    #             ans = tempAnswer.pop()
    #         answer[i] = ans

    # return answer
    for i in range(len(numbers)-2,-1,-1):
        stack = []
        if(numbers[i] < numbers[i+1]):
            answer[i] = numbers[i+1]
            stack.append(answer[i])
        else:
            while(len(stack) != 0 and numbers[i] > stack[-1]):
                answer[i] = stack.pop()
        print(answer)
    return answer
print(solution([9, 1, 5, 3, 6, 2]))