def is_inside(x,y,N,M):
    return 0<x<=N and 0<y<=M
import heapq
import math
from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N,M,H=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
v=[0 for _ in range(11)]
q=[]
sx,sy=0,0
res=0
for i in range(N):
    for j in range(N):
        if a[i][j]==1:
            sx,sy=i,j
        elif a[i][j]==2:
            q.append((i,j))
def cal(sx,sy,dx,dy):
    return abs(sx-dx)+abs(sy-dy)
def go(cnt,x,y,hp):
    global res
    if cal(sx,sy,x,y)<=hp:
        res=max(res,cnt)
    for i in range(len(q)):
        xx,yy=q[i][0],q[i][1]
        if v[i]:continue
        n_hp=hp-cal(x,y,xx,yy)
        if n_hp>=0:
            v[i]=1
            go(cnt+1,xx,yy,n_hp+H)
            v[i]=0
for i,cur in enumerate(q):
    x,y=cur[0],cur[1]
    hp=M-cal(sx,sy,x,y)
    if hp>=0:
        v[i]=1
        go(1,x,y,hp+H)
        v[i]=0
print(res)