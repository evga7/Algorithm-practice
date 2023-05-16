dx=[0,0,1,-1]
dy=[1,-1,0,0]
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
res=0
def go2(x,y):
    cnt=0
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,M):
            if not a[n_x][n_y]:
                cnt+=1
    return cnt
def go(x,y):
    v2=[]
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        v2.append((x,y,go2(x,y)))
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if is_inside(n_x, n_y, N, M) and a[n_x][n_y] and not visited[n_x][n_y]:
                visited[n_x][n_y]=1
                q.append((n_x,n_y))
    return v2

while True:
    cnt=0
    v=[]
    visited=[[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if a[i][j] and not visited[i][j]:
                visited[i][j]=1
                cnt+=1
                v.append(go(i,j))
    if cnt>1:
        break
    if cnt==0:
        print(0)
        exit(0)
    res+=1
    for cur in v:
        for cur2 in cur:
            x,y,cost=cur2[0],cur2[1],cur2[2]
            a[x][y]-=cost
            a[x][y]=max(a[x][y],0)

print(res)