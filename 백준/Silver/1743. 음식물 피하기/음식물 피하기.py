import bisect
import heapq
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N,M,K=map(int,input().split())
a=[[0 for _ in range(M+1)] for _ in range(N+1)]
v=[[0 for _ in range(M+1)] for _ in range(N+1)]
res=0
def go(sx,sy):
    q=deque()
    cnt=0
    q.append((sx,sy))
    while q:
        cnt+=1
        x,y=q.popleft()
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M) and not v[n_x][n_y] and a[n_x][n_y]:
                v[n_x][n_y]=1
                q.append((n_x,n_y))
    global res
    res=max(res,cnt)

for i in range(K):
    x,y=map(int,input().split())
    a[x-1][y-1]=1
for i in range(N):
    for j in range(M):
        if a[i][j] and not v[i][j]:
            v[i][j]=1
            go(i,j)
print(res)