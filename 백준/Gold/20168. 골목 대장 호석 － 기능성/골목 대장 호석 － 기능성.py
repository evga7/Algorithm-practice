import heapq
dx=[0,0,1,-1]
dy=[1,-1,0,0]
import sys
from collections import *
def input():return sys.stdin.readline().rstrip()
N,M,S,E,C=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b,cost=map(int,input().split())
    g[a].append((b,cost))
    g[b].append((a, cost))
q=[]
dist=[[0 for _ in range(N+1)] for _ in range(N+1)]
q.append((0,S,0))
while q:
    cost,x,money=heapq.heappop(q)
    if x==E:
        print(cost)
        exit(0)
    for cur in g[x]:
        nxt=cur[0]
        n_money=money+cur[1]
        n_cost=max(cost,cur[1])
        if n_money<=C and not dist[x][nxt]:
            dist[x][nxt]=1
            heapq.heappush(q,(n_cost,nxt,n_money))
print(-1)