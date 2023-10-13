from collections import *
def solution(plans):
    answer = []
    v = []
    for s, t, p in plans:
        a, b = map(int, t.split(':'))
        v.append((a * 60 + b, s, int(p)))
    v.sort()
    dq=deque()
    idx=0
    t=v[0][0]
    while len(answer)<len(plans):
        t+=1
        if dq and dq[0][0]+dq[0][2]<=t:
            answer.append(dq.popleft()[1])
            dq2=deque()
            while dq:
                a,b,c=dq.popleft()
                dq2.append((t,b,c))
            for cur in dq2:
                dq.append(cur)
        if idx<len(plans) and v[idx][0]<=t:
            dq2=deque()
            if dq:
                a,b,c=dq.popleft()
                dq2.appendleft((t,b,c-(t-a)))
            while dq:
                a,b,c=dq.popleft()
                dq2.append((t,b,c))
            dq2.appendleft(v[idx])
            for cur in dq2:
                dq.append(cur)
            idx+=1
    return answer