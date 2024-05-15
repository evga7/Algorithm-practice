from collections import *
def solution(want, number, discount):
    answer = 0
    c=0
    l=len(want)
    m=defaultdict(int)
    for i in range(l):
        a,b=want[i],number[i]
        m[a]=b
    m2=defaultdict(int)
    for i,cur in enumerate(discount):
        m2[cur]+=1
        if m2[cur]==m[cur]:
            c+=1
        if i-10>=0:
            t=discount[i-10]
            if m2[t]==m[t]:
                c-=1
            m2[t]-=1
        if c==l:
            answer+=1
    return answer