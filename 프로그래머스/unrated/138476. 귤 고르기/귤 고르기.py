from collections import *
def solution(k, tangerine):
    answer = 0
    a=Counter(tangerine).values()
    for cur in sorted(a,reverse=True):
        k-=cur
        answer+=1
        if k<=0:
            break
    return answer