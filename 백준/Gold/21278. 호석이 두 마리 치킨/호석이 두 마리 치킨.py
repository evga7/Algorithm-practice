from collections import *
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
v=[]
res=987654321
res_v=[]
def solve():
    q=deque()
    dist=[987654321 for _ in range(N+1)]
    dist[0]=0
    for cur in v:
        q.append((cur,0))
        dist[cur]=0
    while q:
        x,cost=q.popleft()
        for nxt in g[x]:
            if dist[nxt]>cost+1:
                dist[nxt]=cost+1
                q.append((nxt,cost+1))
    m=0
    global res,res_v

    for i in range(1,N+1):
        m+=dist[i]*2
    if res>m:
        res_v=v[:]
        res=m
def go(idx,cnt):
    if cnt==2:
        solve()
        return
    for i in range(idx,N+1):
        v.append(i)
        go(i+1,cnt+1)
        v.pop()
go(1,0)
print(*res_v,res)