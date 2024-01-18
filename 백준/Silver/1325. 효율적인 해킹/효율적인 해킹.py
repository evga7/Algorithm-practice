import sys
#sys.setrecursionlimit(100000)
from collections import *
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    g[b].append(a)
visited=[False for _ in range(N+1)]
v=[0 for _ in range(N+1)]
m=0
cnt=0
def go(cur):
    q=deque()
    q.append(cur)
    global cnt
    visited[cur]=1
    while q:
        cur=q.popleft()
        cnt+=1
        for nxt in g[cur]:
            if visited[nxt]:continue
            visited[nxt]=1
            q.append(nxt)
for i in range(1,N+1):
    go(i)
    v[i]=cnt
    visited = [False for _ in range(N + 1)]
    cnt=0
m=max(v)
for i in range(1,N+1):
    if m==v[i]:
        print(i,end=' ')