from collections import *
def solution(plans):
    answer = []
    v = []
    for s, t, p in plans:
        a, b = map(int, t.split(':'))
        v.append([a * 60 + b, s, int(p)])
    v.sort()
    dq=deque()
    idx=0
    t=v[0][0]
    while len(answer)<len(plans):
        t+=1
        if dq and dq[0][0]+dq[0][2]<=t:
            answer.append(dq.popleft()[1])
            for i in range(len(dq)):
                dq[i][0]=t    
        if idx<len(plans) and v[idx][0]<=t:
            if dq:
                dq[0][2]-=(t-dq[0][0])
                dq[0][0]=t
            for i in range(1,len(dq)):
                dq[i][0]=t
            dq.appendleft(v[idx])
            idx+=1
    return answer