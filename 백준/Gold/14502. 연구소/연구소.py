
dx = [-1,1,0,0]  # 위 아 오 왼
dy = [0,0,1,-1]
# dx = [-1,-2,-2,-1,1,2,2,1]  # 오 왼 위 아
# dy = [-2,-1,1,2,2,1,-1,-2]
# dx = [-2,-2,0,0,2,2]  # 오 왼 위 아
# dy = [-1,1,-2,2,-1,1]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
import copy
from collections import *
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
block=[]
virus=[]
res=0
v=[]
for i in range(N):
    for j in range(M):
        if not a[i][j]:
            block.append((i,j))
        elif a[i][j]==2:
            virus.append((i,j))
def go2():
    q=deque()
    visited=[[1 for _ in range(M+1)] for _ in range(N+1)]
    for cur in virus:
        x,y=cur[0],cur[1]
        q.append((x,y))
    for cur in block:
        x,y=cur[0],cur[1]
        visited[x][y]=0
    for cur in v:
        x,y=cur[0],cur[1]
        visited[x][y]=1
        a[x][y]=1


    while q:
        x,y=q.popleft()
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M) and not visited[n_x][n_y] and not a[n_x][n_y]:
                visited[n_x][n_y]=1
                q.append((n_x,n_y))
    c=0
    for cur in v:
        x,y=cur[0],cur[1]
        a[x][y]=0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                c+=1
    global res
    res=max(res,c)
            
def go(idx,cnt):
    if cnt==3:
        go2()
        return
    for i in range(idx,len(block)):
        x,y=block[i][0],block[i][1]
        v.append((x,y))
        go(i+1,cnt+1)
        v.pop()
go(0,0)
print(res)
        