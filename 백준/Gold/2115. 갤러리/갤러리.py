def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
dx=[0,1,0,-1]
dy=[1,0,-1,0]

import heapq
import sys
import math
from collections import *
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
res=0
v=[[[0 for _ in range(M)] for _ in range(N)] for _ in range(4)]
def chk(x,y):
    global res
    for i in range(2):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,M) and a[n_x][n_y]=='.':
            for j in range(4):
                x1=x+dx[j]
                y1=y+dy[j]
                x2=n_x+dx[j]
                y2=n_y+dy[j]
                if is_inside(x1,y1,N,M) and is_inside(x2,y2,N,M):
                    if a[x1][y1]=='X' and a[x2][y2]=='X' and not v[j][x1][y1] and not v[j][x2][y2]:
                        v[j][x1][y1],v[j][x2][y2]=1,1
                        res+=1
for i in range(N):
    for j in range(M):
        if a[i][j]=='.':
            chk(i, j)
print(res)