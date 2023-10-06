import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M

import sys
#sys.setrecursionlimit(200000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N=int(input())
M=int(input())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
dist=[987654321 for _ in range(N+1)]
q=[]
S,E=map(int,input().split())
q.append((0,S))
while q:
    cost,x=heapq.heappop(q)
    if dist[x]<cost:continue
    for cur in g[x]:
        nxt,n_cost=cur[0],cur[1]+cost
        if dist[nxt]>n_cost:
            dist[nxt]=n_cost
            heapq.heappush(q,(n_cost,nxt))
print(dist[E])