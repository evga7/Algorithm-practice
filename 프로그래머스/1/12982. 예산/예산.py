def solution(d, budget):
    answer = 0
    d.sort()
    s=0
    for cur in d:
        s+=cur
        if s>budget:break
        answer+=1
    return answer