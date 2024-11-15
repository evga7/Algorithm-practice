from collections import *
import bisect
import re
import sys
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
N,M=map(int,input().split())
m=defaultdict(list)
dist=[[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N-1):
    a,b,c=map(int,input().split())
    m[a].append((b,c))
    m[b].append((a,c))

for i in range(1,N+1):
    q = deque()
    q.append((int(1e10),i))
    dist[i][i]=-1
    while q:
        cost,cur=q.popleft()
        for nxt,c in m[cur]:
            n_cost=min(cost,c)
            if not dist[i][nxt]:
                dist[i][nxt]=n_cost
                q.append((n_cost,nxt))
    dist[i].sort()
while M:
    M-=1
    a,b=map(int,input().split())
    print(N-bisect.bisect_left(dist[b],a)+1)