from collections import *
v=[]
f=0
m=defaultdict(list)
m2=defaultdict(int)
res_v=[]
def go(cur,cnt,l):
    global f
    if f:
        return
    if cnt==l:
        f=1
        for cur in v:
            res_v.append(cur)
        return
    for nxt in m[cur]:
        s=cur+" "+nxt
        if not m2[s]:continue
        m2[s]-=1
        v.append(nxt)
        go(nxt,cnt+1,l)
        m2[s]+=1
        v.pop()
def solution(tickets):
    tickets.sort(key=lambda x:x[1])
    for cur in tickets:
        m[cur[0]].append(cur[1])
        s=cur[0]+' '+cur[1]
        m2[s]+=1
    v.append("ICN")
    go("ICN",0,len(tickets))
    return res_v