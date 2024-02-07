
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
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
visited=[[0 for _ in range(N+1)]for _ in range(N+1)]
st=set()
idx=1
res=987654321
def go2(sx,sy):
    q=deque()
    q.append((0,sx,sy))
    dist=[[987654321 for _ in range(N+1)] for _ in range(N+1)]
    while q:
        cost,x,y=q.popleft()
        if cost>dist[x][y]:continue
        if visited[sx][sy]!=visited[x][y] and a[x][y]:
            return cost
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,N):
                if visited[n_x][n_y]:
                    if dist[n_x][n_y]>cost:
                        q.append((cost,n_x,n_y))
                        dist[n_x][n_y]=cost
                else:
                    if dist[n_x][n_y] > cost+1:
                        q.append((cost+1, n_x, n_y))
                        dist[n_x][n_y] = cost+1
    return 987654321
def go(x,y,idx):
    q=deque()
    visited[x][y]=idx
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,N) and a[n_x][n_y] and not visited[n_x][n_y]:
                visited[n_x][n_y]=idx
                q.append((n_x,n_y))
for i in range(N):
    for j in range(N):
        if a[i][j] and not visited[i][j]:
            go(i,j,idx)
            idx+=1
for i in range(N):
    for j in range(N):
        if a[i][j] and not visited[i][j] in st:
            st.add(a[i][j])
            res=min(res,go2(i,j))
print(res)