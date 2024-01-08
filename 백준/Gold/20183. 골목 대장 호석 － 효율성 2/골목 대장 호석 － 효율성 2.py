import heapq
def is_inside(x,y,N,M):
    return 0<=x<=N and 0<=y<=M

import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M,A,B,C=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))

def go(mid):
    q=[]
    q.append((0,C,A))
    dist = [int(1e15) for _ in range(N + 1)]
    dist[A] = 0
    visited = [0 for _ in range(N + 1)]
    while q:
        cost,money,pos=heapq.heappop(q)
        if pos==B:
            return cost
        if visited[pos] or cost>mid: continue
        visited[pos]=1
        for nxt,go_cost in g[pos]:
            n_cost=max(go_cost,cost)
            if dist[nxt]>n_cost and money-go_cost>=0:
                dist[nxt]=n_cost
                heapq.heappush(q,(n_cost,money-go_cost,nxt))
    return -1
        
left=0
right=int(1e9)
res=-1
while left<=right:
    mid=left+right>>1
    c=go(mid)
    if c>0:
        res=c
        right=mid-1
    else:
        left=mid+1
print(res)