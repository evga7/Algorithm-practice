from collections import *
def solution(N, stages):
    answer = [0 for _ in range(N)]
    l=len(stages)
    c=Counter(stages)
    v=[]
    for i in range(1,N+1):
        if l:
            v.append((c[i]/l,i))
            l-=c[i]
        else:
            v.append((0,i))
    v.sort(key=lambda x:(-x[0],x[1]))
    for i,cur in enumerate(v):
        answer[i]=cur[1]
    return answer