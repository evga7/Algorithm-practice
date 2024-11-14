import heapq
import itertools
import math
from collections import *
import bisect
import re
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1,-1]
dy = [1, -1, 0, 0]
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
visited=[[[0 for _ in range(M+1)] for _ in range(N+1)] for _ in range(4)]
sx,sy,s_dir=map(int,input().split())
ex,ey,e_dir=map(int,input().split())
q=[]
q.append((0,sx-1,sy-1,s_dir-1))
ex-=1
ey-=1
e_dir-=1
visited[s_dir][sx][sy]=1
while q:
    cost,x,y,d=heapq.heappop(q)
    if x==ex and y==ey and d==e_dir:
        print(cost)
        exit(0)
    for i in range(1,4):
        n_x=x+(dx[d]*i)
        n_y=y+(dy[d]*i)
        if is_inside(n_x,n_y,N,M) and a[n_x][n_y]:
            break
        if is_inside(n_x,n_y,N,M) and not a[n_x][n_y] and not visited[d][n_x][n_y]:
            visited[d][n_x][n_y]=1
            heapq.heappush(q,(cost+1,n_x,n_y,d))
    for i in range(4):
        if 0<=d<=1 and i<2:continue
        if 2<=d<=3 and i>2:continue
        if not visited[i][x][y]:
            visited[i][x][y] = 1
            heapq.heappush(q, (cost + 1, x, y,i))