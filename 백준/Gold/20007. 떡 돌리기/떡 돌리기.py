import bisect
import heapq
import itertools
import sys
from collections import *
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]
N,M,X,Y=map(int,input().split())
g=defaultdict(list)
dist=[987654321 for _ in range(N+1)]
q=[]
dist[Y]=0
for i in range(M):
    s,e,cost=map(int,input().split())
    g[s].append((e,cost))
    g[e].append((s,cost))
q.append((0,Y))
while q:
    cost,cur=heapq.heappop(q)
    for nxt,n_c in g[cur]:
        n_cost=cost+n_c
        if dist[nxt]>n_cost:
            dist[nxt]=n_cost
            heapq.heappush(q,(n_cost,nxt))
v=[]
for i in range(N):
    if i==Y:continue
    v.append(dist[i])
    if dist[i]*2>X:
        print(-1)
        exit(0)
v.sort()
s=0
cnt=0
for cur in v:
    if s+(cur*2)>X:
        cnt+=1
        s=0
    s+=cur*2
if s:
    cnt+=1
print(cnt)


