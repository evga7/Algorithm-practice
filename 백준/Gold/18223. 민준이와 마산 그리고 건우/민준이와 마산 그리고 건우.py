from collections import *
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import sys
def input(): return sys.stdin.readline().rstrip()
V,E,P=map(int,input().split())
g=[[] for _ in range(V+1)]
for i in range(E):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))
res1=987654321
res2=0
def go(start,end):
    dist=[987654321 for _ in range(V+1)]
    q=deque()
    q.append((start,0))
    dist[start]=0
    while q:
        x,cost=q.popleft()
        for cur in g[x]:
            nxt,n_cost=cur[0],cur[1]+cost
            if dist[nxt]>n_cost:
                dist[nxt]=n_cost
                q.append((nxt,n_cost))
    return dist[end]
res1=go(1,P)+go(P,V)
res2=go(1,V)
if res1<=res2:
    print("SAVE HIM")
else:
    print("GOOD BYE")