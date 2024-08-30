from collections import *
import math
def solution(a, b, c, d):
    answer = 0
    m=defaultdict(int)
    m[a]+=1
    m[b]+=1
    m[c]+=1
    m[d]+=1
    v=list(m.keys())
    if len(m)==1:
        answer=1111*a
    elif len(m)==2:
        if m[v[0]]==2:
            answer=(v[0]+v[1])*abs(v[0]-v[1])
        else:
            p,q=v[0],v[1]
            if m[q]==3:
                p,q=q,p
            answer=pow(10*p+q,2)
    elif len(m)==3:
        answer=1
        for cur in v:
            if m[cur]==1:
                answer*=cur
    else:
        answer=min(a,b,c,d)
    return answer
