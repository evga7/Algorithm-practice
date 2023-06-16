import heapq
import math


def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
from collections import *
import sys
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
pos=[]
b=[]
p=[i for i in range(M+1)]
for i in range(N):
    for j in range(N):
        if a[i][j]=='S' or a[i][j]=='K':
            pos.append((i,j))
def go(S,E):
    q=deque()
    sx,sy=S[0],S[1]
    ex,ey=E[0],E[1]
    q.append((0,sx,sy))
    v=[[False for _ in range(N)] for _ in range(N)]
    while q:
        cost,x,y=q.popleft()
        if x==ex and y==ey:
            return cost
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,N) and a[n_x][n_y]!='1' and not v[n_x][n_y]:
                v[n_x][n_y]=True
                q.append((cost+1,n_x,n_y))
    return 0
for i in range(M+1):
    for j in range(i+1,M+1):
        c=go(pos[i],pos[j])
        if c:
            b.append((c,i,j))
def find(x):
    if x==p[x]:
        return x
    p[x]=find(p[x])
    return p[x]
def uni(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        p[y]=x
        return True
    return False
res=0
b.sort()
for cur in b:
    if uni(cur[1],cur[2]):
        res+=cur[0]
r=p[0]
for i in range(1,M+1):
    if r!=find(i):
        print(-1)
        exit(0)
print(res)