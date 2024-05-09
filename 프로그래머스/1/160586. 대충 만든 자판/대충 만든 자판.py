from collections import *
def solution(keymap, targets):
    answer = []
    m=defaultdict(int)
    for x in keymap:
        for i,cur in enumerate(x):
            if cur in m:
                m[cur]=min(m[cur],i+1)
            else:
                m[cur]=i+1
    for x in targets:
        c=0
        for cur in x:
            if not cur in m:
                c=-987654321
                break
            c+=m[cur]
        if c<0:
            c=-1
        answer.append(c)
    return answer