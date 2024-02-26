import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
#sys.setrecursionlimit(10000)
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
visited=[0 for _ in range(100001)]
q=[]
q.append((0,N))
visited[N]=1
while q:
    cost,cur=heapq.heappop(q)
    if cur==M:
        print(cost)
        exit(0)
    for nxt in (cur*2,cur+1,cur-1):
        if 0<=nxt<=100000 and not visited[nxt]:
            visited[nxt]=1
            heapq.heappush(q,(cost+1,nxt))