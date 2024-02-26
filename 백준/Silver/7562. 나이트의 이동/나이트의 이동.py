dx = [-1,-2,-2,-1,1,2,2,1]  # 오 왼 위 아
dy = [-2,-1,1,2,2,1,-1,-2]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
sys.setrecursionlimit(10000)
def input():return sys.stdin.readline().rstrip()
T=int(input())
def go():
    q=[]
    q.append((0,sx,sy))
    dist[sx][sy]=0
    while q:
        cost,x,y=heapq.heappop(q)
        for i in range(8):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,N) and dist[n_x][n_y]>cost+1:
                dist[n_x][n_y]=cost+1
                heapq.heappush(q,(cost+1,n_x,n_y))
    print(dist[ddx][ddy])
while T:
    T-=1
    N=int(input())
    sx,sy=map(int,input().split())
    ddx, ddy = map(int, input().split())
    dist=[[987654321 for _ in range(N+1)] for _ in range(N+1)]
    go()