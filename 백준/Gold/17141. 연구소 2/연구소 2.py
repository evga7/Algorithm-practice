dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
v=[]
v2=[]
res=987654321
visited=[0 for _ in range(11)]
for i in range(N):
    for j in range(N):
        if a[i][j]==2:
            v.append((i,j))
def go2():
    dist=[[987654321 for _ in range(N+1)] for _ in range(N+1)]
    q = []
    for cur in v2:
        x,y=cur[0],cur[1]
        q.append((0,x,y))
        dist[x][y]=0
    while q:
        cost,x,y=heapq.heappop(q)
        if dist[x][y]<cost:continue
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,N) and a[n_x][n_y]!=1 and dist[n_x][n_y]>cost+1:
                dist[n_x][n_y]=cost+1
                heapq.heappush(q,(cost+1,n_x,n_y))
    c=0
    for i in range(N):
        for j in range(N):
            if a[i][j]!=1:
                if dist[i][j]==987654321:
                    return 987654321
                c=max(c,dist[i][j])
    return c
        
def go(idx,cnt):
    if cnt==M:
        global res
        res=min(res,go2())
        return
    for i in range(idx,len(v)):
        v2.append(v[i])
        go(i+1,cnt+1)
        v2.pop()
go(0,0)
if res==987654321:
    res=-1

print(res)