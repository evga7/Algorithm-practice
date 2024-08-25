dx = [0,1,0,-1]  # 오 아 왼 위
dy = [1,0,-1,0]
dd=[0,4,2,4,4,1]
import heapq
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import copy
from collections import *
import bisect
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
v=[[0 for _ in range(N+1)] for _ in range(N+1)]
res1,res2=0,0
a=[list(input())for _ in range(N)]
def go(sx,sy,op):
    q=deque()
    q.append((sx,sy))
    while q:
        x,y=q.popleft()
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,N) and a[n_x][n_y]==op and not v[n_x][n_y]:
                v[n_x][n_y]=1
                q.append((n_x,n_y))
for i in range(N):
    for j in range(N):
        if not v[i][j]:
            go(i,j,a[i][j])
            res1+=1
for i in range(N):
    for j in range(N):
        if a[i][j]=='G':
            a[i][j]='R'
v=[[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if not v[i][j]:
            go(i,j,a[i][j])
            res2+=1
print(res1,res2)