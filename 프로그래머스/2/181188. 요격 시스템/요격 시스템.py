def solution(targets):
    answer = 1
    targets.sort(key=lambda x:x[1])
    pos = targets[0][1]-0.1
    for i in range(1,len(targets)):
        s,e=targets[i][0],targets[i][1]
        if s<pos:continue
        answer+=1
        pos=e-0.1
    return answer