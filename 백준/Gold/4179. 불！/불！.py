dx=[0,0,1,-1,-1,1,1,-1]
dy=[1,-1,0,0,1,1,-1,-1]
from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
q=deque()
fx,fy=-1,-1
jx,jy=-1,-1
for i in range(N):
    for j in range(M):
        if a[i][j]=='F':
            q.append((i,j,0))
        elif a[i][j]=='J':
            jx,jy=i,j
    if fx>=0 and jx>=0:break
dist=[[987654321 for _ in range(M+1)] for _ in range(N+1)]
while q:
    x,y,cost=q.popleft()
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if 0<=n_x<N and 0<=n_y<M and dist[n_x][n_y]>cost+1 and a[n_x][n_y]!='#':
            dist[n_x][n_y]=cost+1
            q.append((n_x,n_y,cost+1))
q=deque()
q.append((jx,jy,0))
while q:
    x,y,cost=q.popleft()
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if -1<=n_x<=N and -1<=n_y<=M:
            if not (0<=n_x<N and 0<=n_y<M):
                print(cost+1)
                exit(0)
            if a[n_x][n_y]=='.' and dist[n_x][n_y]>cost+1:
                dist[n_x][n_y]=cost+1
                q.append((n_x,n_y,cost+1))
print("IMPOSSIBLE")