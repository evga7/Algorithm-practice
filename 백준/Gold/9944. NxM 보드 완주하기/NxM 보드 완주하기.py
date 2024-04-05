dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M


import copy
import bisect
import sys
import heapq
from collections import *
#sys.setrecursionlimit(100000)
def slide(x,y,d,v):
    global c
    if not visited[x][y]:
        v.append((x,y))
        visited[x][y]=1
        c+=1
    n_x=x+dx[d]
    n_y=y+dy[d]
    while is_inside(n_x,n_y,N,M) and a[n_x][n_y]=='.' and not visited[n_x][n_y]:
        visited[n_x][n_y]=1
        v.append((n_x, n_y))
        c+=1
        n_x+=dx[d]
        n_y+=dy[d]
    return (n_x-dx[d],n_y-dy[d])
def unSlide(v):
    global c
    for cur in v:
        x,y=cur[0],cur[1]
        visited[x][y]=0
        c-=1
def go(x,y,cc):
    global res,c
    if res<=cc:
        return
    if c==cnt:
        res=min(cc,res)
        return
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,M) and a[n_x][n_y]=='.' and not visited[n_x][n_y]:
            v=[]
            n_x2,n_y2=slide(x,y,i,v)
            go(n_x2,n_y2,cc+1)
            unSlide(v)
idx=0

while True:
    try:
        N, M = map(int,input().split())
    except:
        break
    idx+=1
    visited=[[0 for _ in range(M+1)] for _ in range(N+1)]
    if not N or not M:
        break
    a=[list(input()) for _ in range(N)]
    cnt=0
    c=0
    res=987654321
    for i in range(N):
        for j in range(M):
            if a[i][j]=='.':
                cnt+=1
    for i in range(N):
        for j in range(M):
            if a[i][j]=='.':
                visited[i][j]=1
                c=1
                go(i,j,0)
                visited[i][j]=0
                c=0
    if res==987654321:
        res=-1
    print("Case %d: %d"%(idx,res))
