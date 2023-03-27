from collections import *
def solution(genres, plays):
    answer = []
    m=defaultdict(int)
    m2=defaultdict(list)
    for i in range(len(plays)):
        g=genres[i]
        p=plays[i]
        m[g]+=p
        m2[g].append((p,i))
    for cur in sorted(m.items(),key=lambda x:x[1],reverse=True):
        nxt=sorted(m2[cur[0]],key=lambda x:(-x[0],x[1]))[:2]
        for cur2 in nxt:
            answer.append(cur2[1])
    return answer