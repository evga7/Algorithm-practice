import sys
sys.setrecursionlimit(10 ** 4)
from collections import *
def input():return sys.stdin.readline().rstrip()
N=list(map(int,input()))
dp=[[-1 for _ in range(27)] for _ in range(5001)]
def go(idx,num):
    if idx==len(N):
        return 1
    if dp[idx][num]!=-1:
        return dp[idx][num]
    ret=0
    if N[idx]!=0:
        ret+=go(idx+1,N[idx])%1000000
    if idx+1<len(N):
        nxt=N[idx]*10+N[idx+1]
        if nxt<10:
            return 0
        if 1<=nxt<=26:
            ret+=go(idx+2,nxt)%1000000
    dp[idx][num]=ret
    return dp[idx][num]%1000000
res=0
if N:
    res=max(res,go(0,0))
print(res)