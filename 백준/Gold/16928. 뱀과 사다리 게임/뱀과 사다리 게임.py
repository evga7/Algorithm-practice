import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
import copy
from collections import *
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
dp=[-1 for _ in range(101)]
m=defaultdict(int)
for i in range(N+M):
    a,b=map(int,input().split())
    m[a]=b
q=[]
q.append((0,1))
visited=[0 for _ in range(101)]
while q:
    cost,cur=heapq.heappop(q)
    if cur==100:
        print(cost)
    for i in range(1,7):
        nxt=cur+i
        if nxt<=100 and not visited[nxt]:
            visited[nxt]=1
            if m[nxt]:
                heapq.heappush(q,(cost+1,m[nxt]))
            else:
                heapq.heappush(q, (cost + 1, nxt))