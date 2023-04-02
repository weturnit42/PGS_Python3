def solution(genres, plays):
    answer = []
    
    musicDict = {}
    
    for i in range(len(genres)):
        if(genres[i] not in musicDict):
            musicDict[genres[i]] = [(plays[i], i)]
        else:
            musicDict[genres[i]].append(((plays[i], i)))
            
    genrePlayCount = []
    for key in musicDict:
        musicDict[key].sort(key = lambda x: (-x[0], x[1]))
        temp = 0
        for i in range(len(musicDict[key])):
            temp = temp+musicDict[key][i][0]
        genrePlayCount.append((key, temp))
    genrePlayCount.sort(key = lambda x: -x[1])
    
    for genre in genrePlayCount:
        for i in range(len(musicDict[genre[0]])):
            if(i==2):
                break
            answer.append(musicDict[genre[0]][i][1])
    return answer