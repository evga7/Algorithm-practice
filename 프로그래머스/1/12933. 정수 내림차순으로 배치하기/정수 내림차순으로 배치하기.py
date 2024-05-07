def solution(n):
    v=[]
    while n:
        v.append(n%10)
        n//=10
    v.sort(reverse=True)
    answer=0
    for cur in v:
        answer=answer*10+cur
    return answer