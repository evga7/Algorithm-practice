import heapq
import itertools
import collections
#sys.setrecursionlimit(10 ** 6)
import sys
from collections import *
dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
def is_inside(x,y,N,M):
    return 0<x<=N and 0<y<=M
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
INF = sys.maxsize
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))
for i in range(1,N+1):
    g[i].sort()
S,E=map(int,input().split())
st=[0 for _ in range(N+1)]
visited=[0 for _ in range(N+1)]
def solve(start):
    q=[]
    q.append((0,start))
    dist = [INF for _ in range(N + 1)]
    dist[start]=0
    while q:
        cost,x=heapq.heappop(q)
        for cur in g[x]:
            nxt,n_cost=cur[0],cost+cur[1]
            if dist[nxt]>n_cost and not visited[nxt]:
                dist[nxt]=n_cost
                heapq.heappush(q,(n_cost,nxt))
    return dist
d=solve(E)
first_cost=0
cur=S
while cur != E:
    for  next_node, next_cost in g[cur]:
        if first_cost + next_cost + d[next_node] == d[S]:
            first_cost += next_cost
            visited[next_node]=1
            cur = next_node
            break
visited[E]=0
d2=solve(S)
print(d[S]+d2[E])