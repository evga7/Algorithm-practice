from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
dx=[0,0,1,-1,-1,1,1,-1]
dy=[1,-1,0,0,1,1,-1,-1]
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
sx,sy=-1,-1
for i in range(N):
    for j in range(M):
        if a[i][j]==2:
            sx=i
            sy=j
    if sx!=-1:
        break
v=[[987654321 for _ in range(M)] for _ in range(N)]
q=deque()
q.append((sx,sy,0))
v[sx][sy]=0
while q:
    x,y,c=q.popleft()
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if 0<=n_x<N and 0<=n_y<M and a[n_x][n_y]==1 and v[n_x][n_y]>c+1:
            v[n_x][n_y]=c+1
            q.append((n_x,n_y,c+1))

for i in range(N):
    for j in range(M):
        if v[i][j]==987654321:
            if a[i][j]:
                v[i][j]=-1
            else:
                v[i][j]=0
        print(v[i][j],end=' ')
    print('')
