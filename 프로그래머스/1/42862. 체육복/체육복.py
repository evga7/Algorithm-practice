
from collections import *
def solution(n, lost, reserve):
    c=set(lost)-set(reserve)
    c2=set(reserve)-set(lost)
    c=Counter(c)
    answer = n-len(c)
    for cur in c2:
        left,right=cur-1,cur+1
        if c[left]:
            c[left]-=1
            answer+=1
        elif c[right]:
            c[right]-=1
            answer+=1
    return answer