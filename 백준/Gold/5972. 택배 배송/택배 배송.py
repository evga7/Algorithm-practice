import heapq
import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a, c))

q=[]
dist=[987654321 for _ in range(N+1)]
dist[0]=0
heapq.heappush(q,(0,1))
while q:
    cost,cur=heapq.heappop(q)
    for cur2 in g[cur]:
        nxt=cur2[0]
        n_cost=cost+cur2[1]
        if dist[nxt]>n_cost:
            dist[nxt]=n_cost
            heapq.heappush(q,(n_cost,nxt))
print(dist[N])