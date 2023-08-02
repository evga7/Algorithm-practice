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
block=set()
g=[[] for _ in range(N+1)]
arr=[list(map(int,input().split())) for _ in range(M)]
for a,b,c in arr:
    g[a].append((b,c))
    g[b].append((a,c))
flag=0
st=[0 for _ in range(N+1)]
def go():
    global flag
    q=[]
    q.append((0,1))
    dist = [987654321 for _ in range(N + 1)]
    dist[1]=0
    while q:
        cost,x=heapq.heappop(q)
        if x==N:
            return cost
        if dist[x]<cost:continue
        for nxt,co in g[x]:
            n_cost=cost+co
            if dist[nxt]>n_cost and not (x,nxt) in block and not (nxt,x) in block:
                if not flag:
                    st[nxt]=x
                dist[nxt]=n_cost
                heapq.heappush(q,(n_cost,nxt))
    return 987654321
r=go()
flag=1
r2=0
for i in range(2,N+1):
    a,b=i,st[i]
    block.add((a,b))
    r2=max(r2,go())
    block.remove((a,b))
if r2==987654321:
    res=-1
else:
    res=r2-r
print(res)