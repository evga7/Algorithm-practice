from collections import *
#sys.setrecursionlimit(100000)
dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

import math
import sys
def input():return sys.stdin.readline().rstrip()
MAX=sys.maxsize
M,N=map(int,input().split())
m={'W':0,'B':1}
m2=defaultdict(int)
a=[list(input()) for _ in range(N)]
visited=[[0 for _ in range(M+1)] for _ in range(N+1)]
def go(sx,sy,op):
    q=deque()
    visited[sx][sy]=1
    q.append((sx,sy))
    cnt=0
    while q:
        x,y=q.popleft()
        cnt+=1
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M) and op==a[n_x][n_y] and not visited[n_x][n_y]:
                visited[n_x][n_y]=1
                q.append((n_x,n_y))
    return cnt
res1,res2=0,0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            c=go(i,j,a[i][j])
            if a[i][j]=='W':
                res1+=c*c
            else:
                res2+=c*c
print(res1,res2)