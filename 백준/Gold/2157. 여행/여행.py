import sys
from collections import *
def input():return sys.stdin.readline().rstrip()
N,M,K=map(int,input().split())
dist=[[0 for _ in range(N+1)] for _ in range(N+1)]
g=[[] for _ in range(N+1)]
for i in range(K):
    a,b,cost=map(int,input().split())
    if a>b:continue
    g[a].append((b,cost))
dp=[[-1 for _ in range(N+1)] for _ in range(N+1)]
def go(idx,cnt):
    if cnt>M:
        return -987654321
    if idx==N:
        return 0
    if dp[idx][cnt]!=-1:
        return dp[idx][cnt]
    ret=-987654321
    for cur in g[idx]:
        nxt,cost=cur[0],cur[1]
        ret=max(ret,go(nxt,cnt+1)+cost)
    dp[idx][cnt]=ret
    return dp[idx][cnt]
print(go(1,1))