from collections import *
import sys
sys.setrecursionlimit(10000)
def input():return sys.stdin.readline().rstrip()
N,M,V=map(int,input().split())
g=[[] for _ in range(N+1)]
visited=[0 for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
def dfs(cur):
    print(cur,end=' ')
    visited[cur]=1
    for nxt in g[cur]:
        if visited[nxt]:continue
        dfs(nxt)
def bfs(start):
    q=deque()
    q.append(start)
    visited[start]=1
    while q:
        cur=q.popleft()
        print(cur,end=' ')
        for nxt in g[cur]:
            if visited[nxt]:continue
            visited[nxt]=1
            q.append(nxt)
for i in range(1,N+1):
    g[i].sort()
dfs(V)
visited=[0 for _ in range(N+1)]
print('')
bfs(V)