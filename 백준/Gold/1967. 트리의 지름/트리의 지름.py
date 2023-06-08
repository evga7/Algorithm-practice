from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
g=[[] for _ in range(N+1)]
r=0
for i in range(N-1):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))
dist=[0 for _ in range(N+1)]
q=deque()
q.append((1,0))
s=0
dist[1]=1
while q:
    x,cost=q.popleft()
    for cur in g[x]:
        nxt,c=cur[0],cur[1]
        if not dist[nxt]:
            dist[nxt]=cost+c
            q.append((nxt,cost+c))
idx=0
for i in range(1,N+1):
    if dist[i]>r:
        r=dist[i]
        idx=i
q.append((idx,0))
dist=[0 for _ in range(N+1)]
res=0
dist[idx]=1
while q:
    x,cost=q.popleft()
    res=max(res,cost)
    for cur in g[x]:
        nxt,c=cur[0],cur[1]
        if not dist[nxt]:
            dist[nxt]=cost+c
            q.append((nxt,cost+c))
print(res)