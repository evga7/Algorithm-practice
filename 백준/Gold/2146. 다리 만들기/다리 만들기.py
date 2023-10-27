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
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
dist=[[987654321 for _ in range(N+1)] for _ in range(N+1)]
b=[[0 for _ in range(N+1)] for _ in range(N+1)]
res=987654321
num=1
def go(sx,sy,num):
    q=deque()
    q.append((sx,sy))
    b[sx][sy]=num
    while q:
        x,y=q.popleft()
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,N) and a[x][y]==a[n_x][n_y] and not b[n_x][n_y]:
                q.append((n_x,n_y))
                b[n_x][n_y]=num
def go2(sx,sy,num):
    global res
    q=deque()
    dist[sx][sy]=0
    q.append((0,sx,sy))
    while q:
        cost,x,y=q.popleft()
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,N) and dist[n_x][n_y]>cost+1 and num!=b[n_x][n_y]:
                dist[n_x][n_y]=cost+1
                q.append((cost+1,n_x,n_y))
                if b[n_x][n_y] and b[n_x][n_y]!=num:
                    res=min(res,cost+1)
for i in range(N):
    for j in range(N):
        if a[i][j] and not b[i][j]:
            go(i,j,num)
            num+=1
            
for i in range(N):
    for j in range(N):
        if a[i][j]:
            go2(i,j,b[i][j])
print(res-1)