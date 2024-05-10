from collections import *
gt=defaultdict(int)
gv=defaultdict(int)
ch=defaultdict(int)
m=defaultdict(int)
def solution(friends, gifts):
    answer = 0
    for cur in gifts:
        a,b=cur.split()
        gt[b]+=1
        gv[a]+=1
        ch[cur]+=1
    l=len(friends)
    for i in range(l):
        cur=friends[i]
        for j in range(i+1,l):
            nxt=friends[j]
            a_b=cur+' '+nxt
            b_a=nxt+' '+cur
            if ch[a_b]>ch[b_a]:
                m[cur]+=1
            elif ch[a_b]<ch[b_a]:
                m[nxt]+=1
            else:
                a_score=gv[cur]-gt[cur]
                b_score=gv[nxt]-gt[nxt]
                if a_score>b_score:
                    m[cur]+=1
                elif a_score<b_score:
                    m[nxt]+=1
    mv=m.values()
    if mv:
        answer=max(mv)
    return answer