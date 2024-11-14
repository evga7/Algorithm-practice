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
#dx = [0, -1, 1,0]
#dy = [1, 0, 0, -1]

N,K=map(int,input().split())
dy=[1,-1,K]
a=[list(map(int,input())) for _ in range(2)]
visited=[[0 for _ in range(N+1)] for _ in range(2)]
q=[]
q.append((0,0,0))
while q:
    t,x,y=heapq.heappop(q)
    for i in range(3):
        n_x = x
        if i==2:
            n_x=1-x
        n_y=y+dy[i]
        if n_y>=N:
            print(1)
            exit(0)
        if not visited[n_x][n_y] and t+1<=n_y and a[n_x][n_y]:
            heapq.heappush(q,(t+1,n_x,n_y))
            visited[n_x][n_y]=1
print(0)