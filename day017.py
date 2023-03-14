def solution(today, terms, privacies):
    answer = []
    
    for i in range(len(privacies)):
        term = privacies[i].split()[1]
        j=0
        while(term != terms[j].split()[0]):
            j = j+1
        year = int(privacies[i].split()[0].split(".")[0])
        month = int(privacies[i].split()[0].split(".")[1])
        day = int(privacies[i].split()[0].split(".")[2])
        
        month = month+int(terms[j].split()[1])
        while(month-12 > 0):
            year = year+1
            month = month-12
            
        if(int(today.split('.')[0]) > year):
            answer.append(i+1)
        elif(int(today.split('.')[0]) == year and int(today.split('.')[1]) > month):
            answer.append(i+1)
        elif(int(today.split('.')[0]) == year and int(today.split('.')[1]) == month and int(today.split('.')[2]) >= day):
            answer.append(i+1)
    return answer