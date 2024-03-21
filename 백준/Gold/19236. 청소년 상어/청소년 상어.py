dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]
#dx = [1, -1, 0, 0]  # 아 위 오 왼
#dy = [0, 0, 1, -1]
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
q=[]
a=[[[0,0] for _ in range(4)] for _ in range(4)]
idx=0
for i in range(4):
    temp=list(map(int,input().split()))
    for i in range(0,8,2):
        num,dir=temp[i],temp[i+1]-1
        a[idx][i//2]=[num,dir]
    idx+=1
x,y=0,0
s_dir=a[0][0][1]
res=a[0][0][0]
a[0][0]=[-1,0]
def fishMove(x,y,dir,m):
    n_x=x+dx[dir]
    n_y=y+dy[dir]
    while not is_inside(n_x,n_y,4,4) or not 0<=m[n_x][n_y][0]<=16:
        dir=(dir+1)%8
        n_x=x+dx[dir]
        n_y=y+dy[dir]
    m[x][y][1]=dir
    m[x][y],m[n_x][n_y]=m[n_x][n_y],m[x][y]
def go(x,y,dir,m,point):
    global res
    res=max(res,point)
    for num in range(1,17):
        f=0
        for i in range(4):
            for j in range(4):
                if m[i][j][0]==num:
                    fishMove(i,j,m[i][j][1],m)
                    f=1
                    break
            if f:
                break
    m[x][y][0]=0
    for i in range(3):
        x+=dx[dir]
        y+=dy[dir]
        if not is_inside(x,y,4,4):break
        if not 1<=m[x][y][0]<=16: continue
        n_num,n_dir=m[x][y][0],m[x][y][1]
        m[x][y]=[-1,0]
        temp=copy.deepcopy(m)
        go(x,y,n_dir,temp,point+n_num)
        m[x][y]=[n_num,n_dir]
go(0,0,s_dir,a,res)
print(res)