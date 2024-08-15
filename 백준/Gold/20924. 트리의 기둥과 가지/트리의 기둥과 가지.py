import heapq
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import copy
from collections import *
import bisect
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
dp=[[-1 for _ in range(2001)] for _ in range(2001)]
N,M=map(int,input().split())
g=[[] for _ in range(N+1)]
p=[0 for _ in range(N+1)]
dist=[MAX for _ in range(N+1)]
giga=-1
res1,res2=0,0
for i in range(N-1):
    a,b,c=map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))
    p[a]+=1
    p[b]+=1
def find_giga():
    global giga,res1
    q=deque()
    dist[M]=1
    q.append((M,0))
    while q:
        cur,cost=q.popleft()
        if not dist[cur]:continue
        dist[cur]=0
        cnt=0
        for nxt,c in g[cur]:
            if not dist[nxt]: continue
            cnt+=1
            if cnt==2:
                giga=cur
                res1=cost
                return
            q.append((nxt,cost+c))
        if cnt==0:
            giga=cur
            res1=cost
            return
find_giga()
def go():
    global res2
    q=[]
    q.append((0,giga))
    dist[giga]=0
    while q:
        cost,cur=heapq.heappop(q)
        if dist[cur]<cost:continue
        res2=max(res2,cost)

        for nxt,c in g[cur]:
            n_cost=cost+c
            if dist[nxt]>n_cost:
                dist[nxt]=n_cost
                heapq.heappush(q,(n_cost,nxt))


go()
print(res1,res2)