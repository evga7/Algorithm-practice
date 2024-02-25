dx = [0,0,-1,1]  # 오 왼 위 아
dy = [1,-1,0,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
#sys.setrecursionlimit(10000)
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input()))for _ in range(N)]
dist=[[987654321 for _ in range(M+1)] for _ in range(N+1)]
def go(sx,sy):
    q=[]
    q.append((0,sx,sy))
    dist[sx][sy]=0
    while q:
        cost,x,y=heapq.heappop(q)
        if x==N-1 and y==M-1:
            return cost
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M) and a[n_x][n_y] and dist[n_x][n_y]>cost+1:
                dist[n_x][n_y]=cost+1
                heapq.heappush(q,(cost+1,n_x,n_y))
    return -1
print(go(0,0)+1)