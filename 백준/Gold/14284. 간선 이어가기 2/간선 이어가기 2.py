import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a, c))
S,T=map(int,input().split())
q=[]
q.append((0,S))
dist=[987654321 for _ in range(N+1)]
dist[S]=0
while q:
    cost,x=heapq.heappop(q)
    if x==T:
        print(cost)
        exit(0)
    for cur in g[x]:
        nxt,c=cur[0],cur[1]
        if dist[nxt]>cost+c:
            dist[nxt]=cost+c
            heapq.heappush(q,(cost+c,nxt))