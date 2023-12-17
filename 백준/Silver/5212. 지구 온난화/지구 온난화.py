dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M

import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
b=[[1 for _ in range(M)] for _ in range(N)]
def chk(x,y):
    cnt=0
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if not is_inside(n_x,n_y,N,M):
            cnt+=1
        elif is_inside(n_x,n_y,N,M) and a[n_x][n_y]=='.':
            cnt+=1
    return cnt>=3
for i in range(N):
    for j in range(M):
        if chk(i,j):
            b[i][j]=0
sx=11
sy=11
dx=0
dy=0
for i in range(N):
    for j in range(M):
        if a[i][j]=='X':
            if b[i][j]:
                sy=min(sy,j)
                dy=max(dy,j)
            if b[i][j]:
                sx=min(sx,i)
                dx=max(dx,i)

for i in range(sx,dx+1):
    for j in range(sy,dy+1):
        if b[i][j]:
            print(a[i][j],end='')
        else:
            print('.',end='')
    print('')
if sx==11 and sy==11:
    print('X')