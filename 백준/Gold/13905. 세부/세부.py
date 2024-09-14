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
N,M=map(int,input().split())
S,E=map(int,input().split())
g=defaultdict(list)
for i in range(M):
    s,e,cost=map(int,input().split())
    g[s].append((e,cost))
    g[e].append((s,cost))
dist=[0 for _ in range(N+1)]
q=[]
q.append((-987654321,S))
while q:
    cost,cur=heapq.heappop(q)
    for nxt,cost2 in g[cur]:
        n_cost=min(-cost,cost2)
        if dist[nxt]<n_cost:
            dist[nxt]=n_cost
            heapq.heappush(q,(-n_cost,nxt))
print(dist[E])