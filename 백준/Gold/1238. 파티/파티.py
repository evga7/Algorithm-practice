from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N,M,X=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
def go(start,des):
    q=deque()
    q.append((start,0))
    dist=[987654321 for _ in range(N+1)]
    dist[start]=0
    while q:
        cur,cost=q.popleft()
        for d in g[cur]:
            nxt=d[0]
            n_cost=cost+d[1]
            if dist[nxt]>n_cost:
                dist[nxt]=n_cost
                q.append((nxt,n_cost))
    return dist[des]
res=0
for i in range(1,N+1):
    res=max(res,go(i,X)+go(X,i))
print(res)