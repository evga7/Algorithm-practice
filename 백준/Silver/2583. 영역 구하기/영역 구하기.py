from collections import *
#sys.setrecursionlimit(100000)
dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M


import sys
def input():return sys.stdin.readline().rstrip()
N,M,K=map(int,input().split())
a=[[0 for _ in range(M)] for _ in range(N)]
visited=[[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            a[i][j]=1
v=[]
def go(sx,sy):
    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=1
    cnt=0
    while q:
        x,y=q.popleft()
        cnt+=1
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M) and not a[n_x][n_y] and not visited[n_x][n_y]:
                visited[n_x][n_y]=1
                q.append((n_x,n_y))
    v.append(cnt)
for i in range(N):
    for j in range(M):
        if not a[i][j] and not visited[i][j]:
            go(i,j)
v.sort()
print(len(v))
print(*v)