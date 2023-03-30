import sys
sys.setrecursionlimit(10 ** 6)
d=[[-1 for _ in range(500001)] for _ in range(2)]
def go(op,idx,s):
    if idx>=len(s):
        return 0
    if d[op][idx]!=-1:
        return d[op][idx]
    ret=0
    if op:
        ret=max(ret,go(0,idx+1,s)-s[idx])
    else:
        ret=max(ret,go(1,idx+1,s)+s[idx])
    d[op][idx]=ret
    return d[op][idx]
def solution(sequence):
    answer=0
    for i in range(len(sequence)):
        answer=max(answer,go(1,i,sequence),go(0,i,sequence))
    return answer