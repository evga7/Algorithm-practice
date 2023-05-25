def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import heapq
import sys
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def input():return sys.stdin.readline().rstrip()
a=[list(map(int,input())) for _ in range(8)]
v=[]
for i in range(7):
    for j in range(i,7):
        v.append((i,j))
res=0
visited=[[0 for _ in range(7)] for _ in range(8)]
v2=[set() for _ in range(28)]
def chk(i,j,n_x,n_y,x,y):
    if is_inside(i,j,8,7) and is_inside(n_x,n_y,8,7) and a[i][j]==x and a[n_x][n_y]==y:
        return 1
    return 0
def go(cnt):
    if cnt==28:
        global res
        res+=1
        return
    for cur in v2[cnt]:
        x,y,n_x,n_y=cur[0],cur[1],cur[2],cur[3]
        if not visited[x][y] and not visited[n_x][n_y]:
            visited[x][y],visited[n_x][n_y]=1,1
            go(cnt+1)
            visited[x][y],visited[n_x][n_y]=0,0

for q in range(28):
    x, y = v[q][0], v[q][1]
    for i in range(8):
        for j in range(7):
            for k in range(4):
                n_x = i + dx[k]
                n_y = j + dy[k]
                if chk(i,j,n_x,n_y,x,y):
                    if not (i,j,n_x,n_y) in v2[q] and not (n_x,n_y,i,j) in v2[q]:
                        v2[q].add((i,j,n_x,n_y))
go(0)
print(res)