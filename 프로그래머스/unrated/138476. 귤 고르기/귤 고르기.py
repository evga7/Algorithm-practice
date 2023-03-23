from collections import *
def solution(k, tangerine):
    answer = 0
    m=defaultdict(int)
    for cur in tangerine:
        m[cur]+=1
    for cur in sorted(list(m.values()),key=lambda x:-x):
        k-=cur
        answer+=1
        if k<=0:
            break
    return answer