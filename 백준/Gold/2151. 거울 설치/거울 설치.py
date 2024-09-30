import heapq
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N=int(input())
a=[list(input()) for _ in range(N)]
st=set()
cnt=0
c=[[[987654321 for _ in range(N+1)] for _ in range(N+1)]for _ in range(4)]
sx,sy=-1,-1
ex,ey=-1,-1
for i in range(N):
    for j in range(N):
        if a[i][j]=='#':
            if sx==-1:
                sx,sy=i,j
            else:
                ex,ey=i,j
q=[]
for i in range(4):
    q.append((0,i,sx,sy))
    c[i][sx][sy]=0
while q:
    cost,dir,x,y=heapq.heappop(q)
    if c[dir][x][y]<cost:continue
    if x==ex and y==ey:
        print(cost)
        exit(0)
    if a[x][y]=='!':
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,N) and a[n_x][n_y]!='*':
                if dir==i:
                    n_cost=cost
                else:
                    n_cost=cost+1
                if c[i][n_x][n_y]>n_cost:
                    c[i][n_x][n_y] = n_cost
                    heapq.heappush(q,(n_cost,i,n_x,n_y))
    else:
        n_x,n_y=x+dx[dir],y+dy[dir]
        if is_inside(n_x,n_y,N,N) and c[dir][n_x][n_y]>cost and a[n_x][n_y]!='*':
            c[dir][n_x][n_y]=cost
            heapq.heappush(q,(cost,dir,n_x,n_y))



