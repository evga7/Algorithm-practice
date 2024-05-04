from collections import *
import math
def solution(a, b, c, d):
    answer = 0
    m=defaultdict(int)
    m[a]+=1
    m[b]+=1
    m[c]+=1
    m[d]+=1
    v=[]
    for cur in m.keys():
        v.append((m[cur],cur))
    v.sort(reverse=True)
    if len(m)==1:
        return 1111*a
    elif len(m)==2:
        q,w,e,r=v[0][0],v[1][0],v[0][1],v[1][1]
        if q==3:
            return math.pow(10*e+r,2)
        else:
            return (e+r)*abs(e-r)
    elif len(m)==3:
        e,r=v[1][1],v[2][1]
        return e*r
    else:
        v.sort(key=lambda x:x[1])
        return v[0][1]
    