dx = [-1,1,0,0]  # 위 아 오 왼
dy = [0,0,1,-1]
# dx = [-1,-2,-2,-1,1,2,2,1]  # 오 왼 위 아
# dy = [-2,-1,1,2,2,1,-1,-2]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
import copy
from collections import *
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
res=0
def chk(m):
    global res
    for i in range(N):
        for j in range(N):
            res=max(res,m[i][j])
def go2(m,dir):
    q=[]
    for i in range(N):
        for j in range(N):
            q.append((m[i][j],i,j))
    if dir==0:
        q.sort(key=lambda x:x[1])
    elif dir==1:
        q.sort(key=lambda x:-x[1])
    elif dir==2:
        q.sort(key=lambda x:-x[2])
    else:
        q.sort(key=lambda x:x[2])
    q=deque(q)
    st=set()
    while q:
        cost,x,y=q.popleft()
        n_x=x+dx[dir]
        n_y=y+dy[dir]
        while is_inside(n_x,n_y,N,N):
            if not m[n_x][n_y]:
                m[x][y],m[n_x][n_y]=0,m[x][y]
                x,y=n_x,n_y
            else:
                if m[x][y]==m[n_x][n_y] and not (n_x,n_y) in st:
                    m[x][y]=0
                    m[n_x][n_y]*=2
                    st.add((n_x,n_y))
                break
            n_x = x + dx[dir]
            n_y = y + dy[dir]
    return m


def go(m,cnt):
    chk(m)
    if cnt==5:
        return
    for i in range(4):
        temp=go2(copy.deepcopy(m), i)
        if temp==m:continue
        go(temp,cnt+1)
go(a,0)
print(res)