def solution(numbers):
    answer = ''
    
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])*4
        
    # for i in range(len(numbers)):
    #     while(len(numbers[i]) < 4):
    #         numbers[i] = numbers[i]
    numbers.sort(reverse=True)
    # print(numbers)
    
#     for i in range(len(numbers)):
#         for j in range(len(numbers)):
#             lenDiff = len(numbers[i]) - len(numbers[j])
            
#             if(lenDiff < 0 and numbers[i] < numbers[j] and int(numbers[i])*pow(10, -lenDiff) >= int(numbers[j])):
#                 temp = numbers[i]
#                 numbers[i] = numbers[j]
#                 numbers[j] = temp
    
    for number in numbers:
        answer += number[:len(number)//4]

    if(answer[0] == '0'):
        return '0'
        
    return answer