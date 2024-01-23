import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M

import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
#map(int,input().split())
INF=sys.maxsize
N,M,P=map(int,input().split())
g=[[] for _ in range(N+1)]
pos=[0 for _ in range(N+1)]

for i in range(M):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))
def go(S,E,op):
    q=[]
    q.append((0,S))
    dist = [987654321 for _ in range(N + 1)]
    while q:
        cost,cur=heapq.heappop(q)
        if cur==E:
            return cost
        for x in g[cur]:
            nxt=x[0]
            n_cost=cost+x[1]
            if dist[nxt]>n_cost:
                dist[nxt]=n_cost
                heapq.heappush(q,(n_cost,nxt))
    
if go(1,N,1)==go(1,P,0)+go(P,N,0):
    print("SAVE HIM")
else:
    print("GOOD BYE")