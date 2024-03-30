dx = [0,1,0,-1]  # 오 아 왼 위
dy = [1,0,-1,0]
dd=[0,4,2,4,4,1]
import heapq
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import copy
from collections import *
import bisect
# sys.setrecursionlimit(100000)
import sys
def input():
    return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
v=[]
res=987654321
for i in range(N):
    for j in range(M):
        if 1<=a[i][j]<=5:
            v.append((i,j,a[i][j]))

def cctv_go(x,y,dir,mm):
    n_x = x + dx[dir]
    n_y = y + dy[dir]
    while is_inside(n_x, n_y, N, M) and a[n_x][n_y]!=6:
        mm[n_x][n_y] = 7
        n_x += dx[dir]
        n_y += dy[dir]

def cctv(x,y,op,dir,mm):
    if op==1:
        cctv_go(x,y,dir,mm)
    elif op==2:
        cctv_go(x, y, dir,mm)
        cctv_go(x, y, (dir+2)%4,mm)
    elif op==3:
        cctv_go(x, y, dir,mm)
        cctv_go(x, y, (dir + 1) % 4,mm)
    elif op==4:
        cctv_go(x, y, dir,mm)
        cctv_go(x, y, (dir + 1) % 4,mm)
        cctv_go(x, y, (dir + 2) % 4,mm)
    else:
        cctv_go(x, y, dir,mm)
        cctv_go(x, y, (dir + 1) % 4,mm)
        cctv_go(x, y, (dir + 2) % 4,mm)
        cctv_go(x, y, (dir+3)%4,mm)
def chk(m):
    global res
    cnt=0
    for i in range(N):
        for j in range(M):
            if not m[i][j]:
                cnt+=1
    res=min(res,cnt)
def go(cnt,m):
    if cnt==len(v):
        chk(m)
        return
    x,y,op=v[cnt]
    for i in range(dd[op]):
        mm=copy.deepcopy(m)
        cctv(x,y,op,i,mm)
        go(cnt+1,mm)
go(0,a)
print(res)