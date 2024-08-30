from collections import *
def solution(lines):
    c=[0 for _ in range(201)]
    for x,y in lines:
        for i in range(x,y):
            c[i+100]+=1
    answer=0
    for i in range(201):
        if c[i]>=2:
            answer+=1
    return answer