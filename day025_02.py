def solution(arr):
    answer = []
    
    answer.append(arr[0])
    
    for num in arr[1:]:
        if(answer[-1] == num):
            continue
        else:
            answer.append(num)
    
    return answer