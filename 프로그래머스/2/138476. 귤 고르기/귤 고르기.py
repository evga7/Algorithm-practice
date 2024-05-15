from collections import *
def solution(k, tangerine):
    answer = 0
    c=Counter(tangerine)
    c2=list(c.values())
    c2.sort(reverse=True)
    for cur in c2:
        if k<=0:
            break
        answer+=1
        k-=cur

    return answer