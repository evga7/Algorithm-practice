dx = [0,0,-1,1]  # 오 왼 위 아
dy = [1,-1,0,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
#sys.setrecursionlimit(10000)
def input():return sys.stdin.readline().rstrip()
M,N=map(int,input().split())
a=[list(map(int,input().split()))for _ in range(N)]
dist=[[987654321 for _ in range(M+1)] for _ in range(N+1)]
q=deque()
def go():
    while q:
        cost,x,y=q.popleft()
        if cost>dist[x][y]:continue
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M) and a[n_x][n_y]==0 and dist[n_x][n_y]>cost+1:
                dist[n_x][n_y]=cost+1
                q.append((cost+1,n_x,n_y))
for i in range(N):
    for j in range(M):
        if a[i][j]==1:
            q.append((0,i,j))
            dist[i][j]=0
res=0
go()
for i in range(N):
    for j in range(M):
        if a[i][j]==-1:continue
        if dist[i][j]==987654321:
            print(-1)
            exit(0)
        else:
            res=max(res,dist[i][j])
print(res)