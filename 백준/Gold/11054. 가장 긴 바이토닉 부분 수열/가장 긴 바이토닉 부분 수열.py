import itertools
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
dx=[0,1,0,-1,-1,-1,1,1]
dy=[1,0,-1,0,-1,1,1,-1]
N=int(input())
a=list(map(int,input().split()))
dp=[-1 for _ in range(N+1)]
dp2=[-1 for _ in range(N+1)]
def go(idx):
    if idx==-1:
        return 1
    if dp[idx]!=-1:
        return dp[idx]
    ret=1
    for i in range(idx-1,-1,-1):
        if a[idx]>a[i]:
            ret=max(ret,go(i)+1)
    dp[idx]=ret
    return dp[idx]
def go2(idx):
    if idx==N:
        return 1
    if dp2[idx]!=-1:
        return dp2[idx]
    ret=1
    for i in range(idx+1,N):
        if a[idx]>a[i]:
            ret=max(ret,go2(i)+1)
    dp2[idx]=ret
    return dp2[idx]
for i in range(N):
    go(i)
    go2(i)
res=0
for i in range(N):
    res=max(res,dp[i]+dp2[i]-1)
print(res)

