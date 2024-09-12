import heapq
import itertools
import math
from collections import *
import sys
sys.setrecursionlimit(200000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
dx=[0,1,0,-1,-1,-1,1,1]
dy=[1,0,-1,0,-1,1,1,-1]
N=int(input())
a=list(map(int,input().split()))
g=defaultdict(list)
idx=2
cost=[0]+list(map(int,input().split()))
for cur in a:
    g[cur].append(idx)
    idx+=1
visited=[0 for _ in range(N+1)]
dp=[[-1 for _ in range(2)] for _ in range(N+1)]
def go(cur,op):
    if dp[cur][op]!=-1:
        return dp[cur][op]
    ret=0
    if op:
        for nxt in g[cur]:
            ret+=go(nxt,0)
    else:
        s=0
        for nxt in g[cur]:
            s+=go(nxt,0)
        for nxt in g[cur]:
            s2=(s-go(nxt,0))+(go(nxt,1)+cost[cur]*cost[nxt])
            ret=max(ret,s,s2)
    dp[cur][op]=ret
    return dp[cur][op]
print(go(1,0))