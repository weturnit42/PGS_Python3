def solution(sequence):
    answer = 0
    seq0 = list(map(lambda i: pow(-1, i)*sequence[i], range(len(sequence))))
    seq1 = list(map(lambda i: pow(-1, i+1)*sequence[i], range(len(sequence))))
    
    ansCandidate0 = []
    ansCandidate0.append(seq0[0])
    for i in range(1, len(sequence)):
        ansCandidate0.append(max(seq0[i], ansCandidate0[i-1]+seq0[i]))
        
    ansCandidate1 = []
    ansCandidate1.append(seq1[0])
    for i in range(1, len(sequence)):
        ansCandidate1.append(max(seq1[i], ansCandidate1[i-1]+seq1[i]))
    
    answer = max(max(ansCandidate0), max(ansCandidate1))
    return answer