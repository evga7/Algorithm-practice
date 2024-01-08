import heapq
def is_inside(x,y,N,M):
    return 0<=x<=N and 0<=y<=M

import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M,A,B,C=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))
dist=[987654321 for _ in range(N+1)]
dist[A]=0
visited=[0 for _ in range(N+1)]
def go():
    q=[]
    q.append((0,C,A))
    while q:
        cost,money,pos=heapq.heappop(q)
        if pos==B:
            return cost
        if visited[pos]: continue
        visited[pos]=1
        for nxt,go_cost in g[pos]:
            n_cost=max(go_cost,cost)
            if dist[nxt]>n_cost and money-go_cost>=0:
                dist[nxt]=n_cost
                heapq.heappush(q,(n_cost,money-go_cost,nxt))
    return -1
        
print(go())
