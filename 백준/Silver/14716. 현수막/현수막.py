dx=[-1,-1,-1,0,1,1,1,0]
dy=[0,-1,1,1,1,0,-1,-1]
import copy


import bisect
import heapq
from collections import *
#sys.setrecursionlimit(100000)
#dx = [1, -1, 0, 0]  # 아 위 오 왼
#dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

import math
import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
MOD=int(1e9)+9
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
v=[[0 for _ in range(M+1)] for _ in range(N+1)]
def go(sx,sy):
    q=deque()
    q.append((sx,sy))
    v[sx][sy]=1
    while q:
        x,y=q.popleft()
        for i in range(8):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M) and not v[n_x][n_y] and a[n_x][n_y]:
                v[n_x][n_y]=1
                q.append((n_x,n_y))
res=0
for i in range(N):
    for j in range(M):
        if a[i][j] and not v[i][j]:
            go(i,j)
            res+=1
print(res)