from collections import *

def solution(players, callings):
    answer = []
    m=defaultdict(str)
    m2=defaultdict(int)
    for i,cur in enumerate(players):
        m[cur]=i+1
        m2[i+1]=cur
    for cur in callings:
        pos=m[cur]
        back=m2[pos-1]
        m2[pos-1],m2[pos]=m2[pos],m2[pos-1]
        m[back],m[cur]=m[cur],m[back]
    for cur in sorted(m.values()):
        answer.append(m2[cur])
    return answer