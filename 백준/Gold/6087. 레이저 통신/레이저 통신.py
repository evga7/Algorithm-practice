dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
import heapq
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import copy
from collections import *
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
M,N=map(int,input().split())
a=[list(input()) for _ in range(N)]
visited=[[[[0 for _ in range(4)] for _ in range(4)] for _ in range(M+1)] for _ in range(N+1)]
sx,sy=-1,-1
ex,ey=-1,-1
for i in range(N):
    for j in range(M):
        if a[i][j]=='C':
            if sx==-1:
                sx,sy=i,j
            else:
                ex,ey=i,j
    if ex!=-1:
        break
q=[]
for i in range(4):
    q.append((0,sx,sy,i))
while q:
    cost,x,y,d=heapq.heappop(q)
    if (x,y)==(ex,ey):
        print(cost)
        exit(0)
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if not is_inside(n_x,n_y,N,M):continue
        if a[n_x][n_y]=='*':continue
        if (x and -x==n_x) or (y and -y==n_y):continue
        if visited[n_x][n_y][d][i]:continue
        visited[n_x][n_y][d][i]=1
        if d!=i:
            heapq.heappush(q,(cost+1,n_x,n_y,i))
        else:
            heapq.heappush(q,(cost,n_x,n_y,d))