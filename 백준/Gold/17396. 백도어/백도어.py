import heapq
from collections import *
#sys.setrecursionlimit(100000)
dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

import math
import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
N,M=map(int,input().split())
a=list(map(int,input().split()))
a[N-1]=0
g=[[] for _ in range(N+1)]
for i in range(M):
    q,w,e=map(int,input().split())
    g[q].append((w,e))
    g[w].append((q,e))
dist=[MAX for _ in range(N+1)]
q=[]
q.append((0,0))
while q:
    cost,cur=heapq.heappop(q)
    if dist[cur]<cost:continue
    if cur==N-1:
        print(cost)
        exit(0)
    for x in g[cur]:
        nxt,n_cost=x[0],cost+x[1]
        if not a[nxt] and dist[nxt]>n_cost:
            dist[nxt]=n_cost
            heapq.heappush(q,(n_cost,nxt))
print(-1)