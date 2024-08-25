dx = [0,1,0,-1,0,0]  # 오 아 왼 위
dy = [1,0,-1,0,0,0]
dz=[0,0,0,0,-1,1]
dd=[0,4,2,4,4,1]
import heapq
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
def is_inside2(x, y,z, N, M,H):
    return 0 <= x < N and 0 <= y < M and 0<=z<H
import copy
from collections import *
import bisect
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
M,N,H=map(int,input().split())
g=[]
v=[[[987654321 for _ in range(M+1)] for _ in range(N+1)]for _ in range(H+1)]
q=deque()
for i in range(H):
    a=[list(map(int,input().split())) for _ in range(N)]
    g.append(a)
for i in range(H):
    for j in range(N):
        for k in range(M):
            cur= g[i][j][k]
            if cur==-1 or cur==1:
                v[i][j][k]=0
                if cur==1:
                    q.append((0,j,k,i))
while q:
    cost,x,y,z=q.popleft()
    for i in range(6):
        n_h=z+dz[i]
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside2(n_x,n_y,n_h,N,M,H) and not g[n_h][n_x][n_y]:
            if v[n_h][n_x][n_y]>cost+1:
                v[n_h][n_x][n_y]=cost+1
                q.append((cost+1,n_x,n_y,n_h))
res=0
for i in range(H):
    for j in range(N):
        for k in range(M):
            cur= g[i][j][k]
            if cur==-1:continue
            cur2=v[i][j][k]
            res=max(res,cur2)
if res==987654321:
    res=-1
print(res)