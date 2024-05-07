from collections import *
m=defaultdict(int)
def solution(s):
    answer = []
    for i,cur in enumerate(s):
        r=-1
        if cur in m:
            r=i-m[cur]
        m[cur]=i
        answer.append(r)
    return answer