def solution(s):
    a=list(map(int,s.split()))
    a.sort()
    answer=str(a[0])+' '+str(a[len(a)-1])
    return answer