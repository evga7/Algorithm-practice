import sys
sys.setrecursionlimit(10 ** 6)
d=[-1 for _ in range(100001)]
def g(idx,s,m):
    if idx>=m:
        return 0
    if d[idx]!=-1:
        return d[idx]
    ret=0
    ret=max(ret,g(idx+2,s,m)+s[idx],g(idx+1,s,m))
    d[idx]=ret
    return d[idx]
def solution(sticker):
    l=len(sticker)
    answer=sticker[0]
    answer=max(answer,g(1,sticker,l))
    global d
    d = [-1 for _ in range(100001)]
    answer = max(answer, g(0, sticker, l-1))
    return answer
