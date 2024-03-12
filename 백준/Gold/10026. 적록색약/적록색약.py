dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
import heapq
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import copy
from collections import *
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[list(input()) for _ in range(N)]
visited=[[0 for _ in range(N+1)] for _ in range(N+1)]
m=defaultdict(int)
m['R']=1
m['G']=2
m['B']=3
def go(sx,sy):
    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,N) and not visited[n_x][n_y] and m[a[sx][sy]]==m[a[n_x][n_y]]:
                visited[n_x][n_y]=1
                q.append((n_x,n_y))

res1=0
res2=0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            go(i,j)
            res1+=1
m['G']=1
visited=[[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            go(i,j)
            res2+=1
print(res1,res2)