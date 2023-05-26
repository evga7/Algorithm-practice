import sys
from collections import *
def input():return sys.stdin.readline().rstrip()
res=-987654321
N=int(input())
a=[int(input()) for _ in range(N)]
a.sort()
dp=[[-987654321 for _ in range(2)]for _ in range(N)]
def go(idx,op):
    if idx==N:
        return 0
    if dp[idx][op]!=-987654321:
        return dp[idx][op]
    ret=-987654321
    if idx+1<N:
        ret=max(ret,go(idx+2,1)+a[idx]*a[idx+1])
    ret=max(ret,go(idx+1,0)+a[idx])
    dp[idx][op]=ret
    return dp[idx][op]
print(go(0,0))