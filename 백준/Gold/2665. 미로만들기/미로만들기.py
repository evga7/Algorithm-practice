dx=[0,0,1,-1]
dy=[1,-1,0,0]
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
arr=[list(map(int,input())) for _ in range(N)]
dist=[[987654321 for _ in range(N)] for _ in range(N)]
q=deque()
q.append((0,0,0))
while q:
    x,y,cost=q.popleft()
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,N):
            n_cost=cost
            if not arr[n_x][n_y]:
                n_cost+=1
            if dist[n_x][n_y]>n_cost:
                dist[n_x][n_y]=n_cost
                q.append((n_x,n_y,n_cost))
print(dist[N-1][N-1])