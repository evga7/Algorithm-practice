from collections import *
def solution(lines):
    m=defaultdict(int)
    answer=0
    for x,y in lines:
        for c in range(x,y):
            m[c]+=1
    for cur in sorted(m.values()):
        if cur>1:
            answer+=1
    return answer
