from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N,M,S=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
v=[0 for _ in range(N+1)]
def go(cur):
    print(cur,end=' ')
    for nxt in g[cur]:
        if v[nxt]:continue
        v[nxt]=1
        go(nxt)
for i in range(N+1):
    g[i].sort()
v[S]=1
go(S)

v=[0 for _ in range(N+1)]
q=deque()
q.append(S)
v[S]=1
print('')
while q:
    x=q.popleft()
    print(x,end=' ')
    for nxt in g[x]:
        if not v[nxt]:
            v[nxt]=1
            q.append(nxt)