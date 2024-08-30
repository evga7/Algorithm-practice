def solution(babbling):
    answer = 0
    a=['aya','ye','woo','ma']
    for cur in babbling:
        s=cur
        for cur2 in a:
            s=s.replace(cur2,' ')
        s=s.replace(' ','')
        if not s:
            answer+=1
    return answer