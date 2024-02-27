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
M,N=map(int,input().split())
a=[list(map(int,input())) for _ in range(N)]
q=[]
q.append((0,0,0))
dist=[[987654321 for _ in range(M+1)] for _ in range(N+1)]
while q:
    cost,x,y=heapq.heappop(q)
    if x==N-1 and y==M-1:
        print(cost)
        exit(0)
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,M):
            n_cost=cost
            if a[n_x][n_y]:
                n_cost=cost+1
            if dist[n_x][n_y]>n_cost:
                heapq.heappush(q,(n_cost,n_x,n_y))
                dist[n_x][n_y]=n_cost