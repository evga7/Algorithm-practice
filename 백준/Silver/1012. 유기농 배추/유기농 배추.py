from collections import *
from functools import cmp_to_key
from typing import List

dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M

import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
#map(int,input().split())
INF=sys.maxsize
T=int(input())
def go(sx,sy):
    q=deque()
    q.append((sx,sy))
    while q:
        x,y=q.popleft()
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M) and not visited[n_x][n_y] and a[n_x][n_y]:
                visited[n_x][n_y]=1
                q.append((n_x,n_y))
while T:
    T-=1
    M,N,K=map(int,input().split())
    a=[[0 for _ in range(M+1)] for _ in range(N+1)]
    visited = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for i in range(K):
        c,d=map(int,input().split())
        a[d][c]=1
    res=0
    for i in range(N):
        for j in range(M):
            if a[i][j] and not visited[i][j]:
                go(i,j)
                res+=1
    print(res)