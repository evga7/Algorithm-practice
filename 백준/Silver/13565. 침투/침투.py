from collections import *
from functools import cmp_to_key
from typing import List

dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M

import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
a=[list(map(int,input())) for _ in range(N)]
visited=[[0 for _ in range(M+1)] for _ in range(N+1)]
def go(sx,sy):
    q=deque()
    visited[sx][sy]=1
    q.append((sx,sy))
    while q:
        x,y=q.popleft()
        if x==N-1:
            print("YES")
            exit(0)
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M) and not visited[n_x][n_y] and not a[n_x][n_y]:
                visited[n_x][n_y]=1
                q.append((n_x,n_y))
    
for i in range(M):
    go(0,i)
print("NO")