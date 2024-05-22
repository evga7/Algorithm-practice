from collections import *
def solution(msg):
    answer = []
    m=defaultdict(int)
    idx=1
    for i in range(26):
        m[chr(i+ord('A'))]=idx
        idx+=1
    idx2=0
    while idx2<len(msg):
        s=""
        while idx2<len(msg):
            bs=s
            s+=msg[idx2]
            if not s in m:
                break
            idx2+=1
        if s in m:
            answer.append(m[s])
        else:
            answer.append(m[bs])
        m[s]=idx
        idx+=1
    return answer