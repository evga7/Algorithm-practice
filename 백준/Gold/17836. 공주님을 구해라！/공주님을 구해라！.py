dx=[0,0,1,-1,-1,1,1,-1]
dy=[1,-1,0,0,1,1,-1,-1]
from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
def is_inside(x,y):
    return 0<=x<N and 0<=y<M
N,M,T=map(int,input().split())

sx,sy=-1,-1
a=[list(map(int,input().split())) for _ in range(N)]
res=T+1
for i in range(N):
    for j in range(M):
        if a[i][j]==2:
            sx,sy=i,j
            break
    if sx>=0:
        break
def go(xx,yy,dxx,dyy,b):
    q=deque()
    q.append((xx,yy,0))
    dist = [[T+1 for _ in range(M + 1)] for _ in range(N + 1)]
    while q:
        x,y,cost=q.popleft()
        if x==dxx and y==dyy:
            return cost
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y) and cost+1<=T:
                if b:
                    if dist[n_x][n_y]>cost+1:
                        dist[n_x][n_y]=cost+1
                        q.append((n_x,n_y,cost+1))
                else:
                    if a[n_x][n_y]!=1 and dist[n_x][n_y]>cost+1:
                        dist[n_x][n_y]=cost+1
                        q.append((n_x,n_y,cost+1))
    return T+1
res=min(res,go(0,0,N-1,M-1,0),go(0,0,sx,sy,0)+go(sx,sy,N-1,M-1,1))
if res>T:
    print("Fail")
else:
    print(res)