dx = [-1,1,0,0]  # 위 아 오 왼
dy = [0,0,1,-1]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
import copy
from collections import *
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input())) for _ in range(N)]
dist=[[[987654321 for _ in range(2)] for _ in range(M+1)] for _ in range(N+1)]
q=deque()
q.append((1,0,0,0))
while q:
    cost,x,y,block=q.popleft()
    if x==N-1 and y==M-1:
        print(cost)
        exit(0)
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,M):
            if a[n_x][n_y] and not block and dist[n_x][n_y][1]>cost+1:
                dist[n_x][n_y][1]=cost+1
                q.append((cost+1,n_x,n_y,1))
            elif not a[n_x][n_y] and dist[n_x][n_y][block]>cost+1:
                dist[n_x][n_y][block]=cost+1
                q.append((cost + 1, n_x, n_y, block))
print(-1)