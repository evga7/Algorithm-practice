import heapq
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import copy
from collections import *
import bisect
# sys.setrecursionlimit(100000)
import sys
def input():
    return sys.stdin.readline().rstrip()
N,M,A,B,C=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))
left=0
right=C
def go(mid):
    dist=[9876543210 for _ in range(N+1)]
    q=[]
    q.append((0,A))
    while q:
        cost,cur=heapq.heappop(q)
        if dist[cur]<cost:continue
        if cur==B:
            return True
        for x in g[cur]:
            nxt,n_cost=x[0],x[1]+cost
            if x[1]<=mid and n_cost<=C and dist[nxt]>n_cost :
                dist[nxt]=n_cost
                heapq.heappush(q,(n_cost,nxt))
res=987654321
while left<=right:
    mid=left+right>>1
    if go(mid):
        right=mid-1
        res=min(res,mid)
    else:
        left=mid+1
if res==987654321:
    res=-1
print(res)
