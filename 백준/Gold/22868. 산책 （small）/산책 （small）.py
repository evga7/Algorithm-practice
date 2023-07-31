import sys
from collections import *
dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
def is_inside(x,y,N,M):
    return 0<x<=N and 0<y<=M
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
for i in range(1,N+1):
    g[i].sort()
S,E=map(int,input().split())

st=[0 for _ in range(N+1)]
visited=[0 for _ in range(N+1)]
def solve(start,end):
    q=deque()
    q.append((start,0))
    visited[start]=0
    visited[end]=0
    dist = [987654321 for _ in range(N + 1)]
    while q:
        x,cost=q.popleft()
        for nxt in g[x]:
            if dist[nxt]>cost+1 and not visited[nxt]:
                st[nxt]=x
                dist[nxt]=cost+1
                q.append((nxt,cost+1))
    cur=st[end]
    while cur!=start:
        visited[cur]=1
        cur=st[cur]
    return dist[end]
res1=solve(S,E)
print(res1+solve(E,S))