def solution(answers):
    answer = []
    
    correct = [0, 0, 0]
    
    for i in range(len(answers)):
        if(answers[i] == i%5+1):
            correct[0] = correct[0]+1
        if((i%2 == 0 and answers[i] == 2)
           or (i%8 == 1 and answers[i] == 1) 
           or (i%8 == 3 and answers[i] == 3) 
           or (i%8 == 5 and answers[i] == 4) 
           or (i%8 == 7 and answers[i] == 5)):
            correct[1] = correct[1]+1
        if(((i%10 == 0 or i%10 == 1) and answers[i] == 3)
           or ((i%10 == 2 or i%10 == 3) and answers[i] == 1)
           or ((i%10 == 4 or i%10 == 5) and answers[i] == 2)
           or ((i%10 == 6 or i%10 == 7) and answers[i] == 4)
           or ((i%10 == 8 or i%10 == 9) and answers[i] == 5)):
            correct[2] = correct[2]+1
            
    maxCorrect = max(correct)
    # print(correct)
    for i in range(len(correct)):
        if(correct[i] == maxCorrect):
            answer.append(i+1)

    return answer