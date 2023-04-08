def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        temp = array[i-1:j]
        temp.sort()
        temp = temp[k-1]
        answer.append(temp)
    return answer