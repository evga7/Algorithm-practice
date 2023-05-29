def is_inside(x,y,N,M):
    return 0<x<=N and 0<y<=M
dx=[0,1,0,-1]
dy=[1,0,-1,0]

import heapq
import math
from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N,M,A,B,K=map(int,input().split())
a=[[0 for _ in range(M+1)] for _ in range(N+1)]
dist=[[987654321 for _ in range(M+1)] for _ in range(N+1)]
for i in range(K):
    x,y=map(int,input().split())
    a[x][y]=1
sx,sy=map(int,input().split())
ex,ey=map(int,input().split())
q=[]
q.append((0,sx,sy))
dist[sx][sy]=0
def chk(x,y):
    if not is_inside(x+A-1,y+B-1,N,M):
        return False
    for i in range(x,x+A):
        for j in range(y,y+B):
            if a[i][j]:
                return False
    return True
while q:
    cost,x,y=heapq.heappop(q)
    if x==ex and y==ey:
        print(cost)
        exit(0)
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,M) and chk(n_x,n_y):
            if dist[n_x][n_y]>cost+1:
                dist[n_x][n_y]=cost+1
                heapq.heappush(q,(cost+1,n_x,n_y))
print(-1)