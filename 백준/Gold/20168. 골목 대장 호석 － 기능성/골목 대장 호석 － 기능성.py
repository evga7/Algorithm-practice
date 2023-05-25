import sys
from collections import *
def input():return sys.stdin.readline().rstrip()
N,M,S,E,C=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b,cost=map(int,input().split())
    g[a].append((b,cost))
    g[b].append((a, cost))
q=deque()
dist=[987654321 for _ in range(N+1)]
q.append((S,0,0))
while q:
    x,cost,money=q.popleft()
    if x==E:
        print(cost)
        exit(0)
    for cur in g[x]:
        nxt=cur[0]
        n_money=money+cur[1]
        n_cost=max(cost,cur[1])
        if n_money<=C and dist[nxt]>n_cost:
            dist[nxt]=n_cost
            q.append((nxt,n_cost,n_money))
print(-1)