from collections import *
import heapq
import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(N-1):
    a,b,cost=map(int,input().split())
    g[a].append((b,cost))
    g[b].append((a, cost))
def go(a,b):
    v=[987654321 for _ in range(N+1)]
    q=deque()
    q.append((a,0))
    while q:
        x,cost=q.popleft()
        if x==b:
            return cost
        for cur in g[x]:
            nxt=cur[0]
            n_cost=cost+cur[1]
            if v[nxt]>n_cost:
                v[nxt]=n_cost
                q.append((nxt,n_cost))
for i in range(M):
    a,b=map(int,input().split())
    print(go(a,b))