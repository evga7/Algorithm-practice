import heapq
import itertools
import collections
#sys.setrecursionlimit(10 ** 6)
import sys
from collections import *
dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
def is_inside(x,y,N,M):
    return 0<x<=N and 0<y<=M
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
dp=[-1 for _ in range(N+1)]
g=[[] for _ in range(N+1)]
arr=list(map(int,input().split()))
arr[N-1]=0
dist=[INF for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))
def go():
    q=[]
    q.append((0,0))
    while q:
        cost,cur=heapq.heappop(q)
        if dist[cur]<cost:continue
        if cur==N-1:
            return cost
        for nxt,co in g[cur]:
            if dist[nxt]>cost+co and not arr[nxt]:
                dist[nxt]=cost+co
                heapq.heappush(q,(cost+co,nxt))
    return -1

print(go())