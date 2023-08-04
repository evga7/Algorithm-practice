import sys
from collections import *
dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
v=[[0 for _ in range(M+1)] for _ in range(N+1)]
def chk(x,y,op):
    s=arr[x][y]
    if op==0:
        if is_inside(x,y+1,N,M) and is_inside(x-1,y,N,M) and is_inside(x+1,y,N,M):
            return s+arr[x][y+1]+arr[x-1][y]+arr[x+1][y]
    elif op==1:
        if is_inside(x-1,y,N,M) and is_inside(x,y-1,N,M) and is_inside(x,y+1,N,M):
            return s+arr[x-1][y]+arr[x][y-1]+arr[x][y+1]
    elif op==2:
        if is_inside(x-1,y,N,M) and is_inside(x+1,y,N,M) and is_inside(x,y-1,N,M):
            return s+arr[x-1][y]+arr[x+1][y]+arr[x][y-1]
    else:
        if is_inside(x,y+1,N,M) and is_inside(x,y-1,N,M) and is_inside(x+1,y,N,M):
            return s+arr[x][y+1]+arr[x][y-1]+arr[x+1][y]
    return 0
res=0
def go(x,y,cnt,s):
    if cnt==4:
        global res
        res=max(res,s)
        return
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,M) and not v[n_x][n_y]:
            v[n_x][n_y]=1
            go(n_x,n_y,cnt+1,s+arr[n_x][n_y])
            v[n_x][n_y]=0

for i in range(N):
    for j in range(M):
        v[i][j]=1
        go(i,j,1,arr[i][j])
        v[i][j]=0
        for k in range(4):
            res=max(res,chk(i,j,k))
print(res)