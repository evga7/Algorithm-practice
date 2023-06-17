import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
N,M,X,Y=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))
q=[]
q.append((0,Y))
dist=[987654321 for _ in range(N)]
dist[Y]=0
while q:
    cost,x=heapq.heappop(q)
    for cur in g[x]:
        nxt,c=cur[0],cur[1]
        if dist[nxt]>cost+c:
            dist[nxt]=cost+c
            heapq.heappush(q,(cost+c,nxt))
dist.sort()
res=0
cnt=0
for i in range(N):
    cost=dist[i]*2
    if cost>X:
        print(-1)
        exit(0)
    if cnt+cost<=X:
        cnt+=cost
    else:
        res+=1
        cnt=cost
if cnt:
    res+=1
print(res)