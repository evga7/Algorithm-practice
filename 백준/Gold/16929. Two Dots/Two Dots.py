dx = [0,0,-1,1]  # 오 왼 위 아
dy = [1,-1,0,0]
# dx = [-1,-2,-2,-1,1,2,2,1]  # 오 왼 위 아
# dy = [-2,-1,1,2,2,1,-1,-2]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
#sys.setrecursionlimit(10000)
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
visited=[[0 for _ in range(M+1)] for _ in range(N+1)]
sx,sy=0,0
def go(x,y,op,cnt):
    if x==sx and y==sy and cnt>=4:
        print("Yes")
        exit(0)
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,M) and not visited[n_x][n_y] and op==a[n_x][n_y]:
            visited[n_x][n_y]=1
            go(n_x,n_y,op,cnt+1)
            visited[n_x][n_y]=0
                
for i in range(N):
    for j in range(M):
        sx,sy=i,j
        go(i,j,a[i][j],1)
print("No")