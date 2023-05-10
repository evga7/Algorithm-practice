dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
v=[]
v.append((N-1,0))
v.append((N-1,1))
v.append((N-2,0))
v.append((N-2,1))
def go(idx,cnt):
    temp=[]
    m=defaultdict(int)
    global v

    for cur in v:
        x,y=cur[0],cur[1]
        n_x=(x+dx[idx]*cnt+N)%N
        n_y=(y+dy[idx]*cnt+N)%N
        temp.append((n_x,n_y))
        a[n_x][n_y]+=1
    for cur in temp:
        x,y=cur[0],cur[1]
        m[(x,y)]+=1
        for j in range(1,8,2):
            n_x=x+dx[j]
            n_y=y+dy[j]
            if is_inside(n_x,n_y,N,N) and a[n_x][n_y]:
                a[x][y]+=1

    v=[]
    for i in range(N):
        for j in range(N):
            if a[i][j]>=2 and not (i,j) in m:
                v.append((i,j))
                a[i][j]-=2
for i in range(M):
    c,d=map(int,input().split())
    go(c-1,d)
res=0
for i in range(N):
    for j in range(N):
        res+=a[i][j]
print(res)