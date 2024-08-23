import heapq
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import copy
from collections import *
import bisect
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
T=int(input())
def go():
    q=[]
    for i in range(1,N+1):
        if not p[i]:
            q.append((a[i-1],i))
            dist[i]=a[i-1]
    while q:
        cost,cur=heapq.heappop(q)
        if dist[cur]<cost:continue
        for nxt in g[cur]:
            p[nxt]-=1
            n_cost=cost+a[nxt-1]
            if not p[nxt] and dist[nxt]>n_cost:
                heapq.heappush(q,(n_cost,nxt))
                dist[nxt]=n_cost

while T:
    T-=1
    g=defaultdict(list)
    N,M=map(int,input().split())
    p=[0 for _ in range(N+1)]
    a=list(map(int,input().split()))
    for i in range(M):
        q,w=map(int,input().split())
        g[q].append(w)
        p[w]+=1
    W=int(input())
    dist=[987654321 for _ in range(N+1)]
    go()
    print(dist[W])