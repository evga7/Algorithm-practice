import heapq
import itertools
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
dx=[0,1,0,-1,-1,-1,1,1]
dy=[1,0,-1,0,-1,1,1,-1]
V,E=map(int,input().split())
g=defaultdict(list)
for i in range(E):
    s,e,cost=map(int,input().split())
    g[s].append((e,cost))
    g[e].append((s, cost))
M,X=map(int,input().split())
mac=list(map(int,input().split()))
S,Y=map(int,input().split())
star=list(map(int,input().split()))
q=[]
dist=[987654321 for _ in range(V+1)]
st=set(star+mac)
for cur in mac:
    q.append((0,cur))
while q:
    cost,cur=heapq.heappop(q)
    if dist[cur]<cost:continue
    for nxt,n_c in g[cur]:
        n_cost=n_c+cost
        if n_cost<=X and n_cost<dist[nxt]:
            dist[nxt]=n_cost
            heapq.heappush(q,(n_cost,nxt))
dist2=[987654321 for _ in range(V+1)]
for cur in star:
    q.append((0,cur))
while q:
    cost,cur=heapq.heappop(q)
    if dist2[cur]<cost:continue
    for nxt,n_c in g[cur]:
        n_cost=n_c+cost
        if n_cost<=Y and n_cost<dist2[nxt]:
            dist2[nxt]=n_cost
            heapq.heappush(q,(n_cost,nxt))
res=987654321
for i in range(1,V+1):
    if i in st:continue
    if dist[i]<=X and dist2[i]<=Y:
        res=min(res,dist[i]+dist2[i])
if res==987654321:
    res=-1
print(res)