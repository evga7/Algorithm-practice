dx = [0,0,-1,1]  # 오 왼 위 아
dy = [1,-1,0,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
#sys.setrecursionlimit(10000)
def input():return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input()))for _ in range(N)]
visited=[[0 for _ in range(N+1)] for _ in range(N+1)]
def go(sx,sy):
    q=deque()
    cnt=0
    q.append((sx,sy))
    visited[sx][sy]=1
    while q:
        x,y=q.popleft()
        cnt+=1
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,N) and not visited[n_x][n_y] and a[n_x][n_y]:
                visited[n_x][n_y]=1
                q.append((n_x,n_y))
    return cnt
v=[]
for i in range(N):
    for j in range(N):
        if not visited[i][j] and a[i][j]:
            v.append(go(i,j))
v.sort()
print(len(v))
for cur in v:
    print(cur)