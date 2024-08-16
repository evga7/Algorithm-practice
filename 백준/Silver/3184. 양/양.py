dx = [0,0,-1,1]  # 오 왼 위 아
dy = [1,-1,0,0]
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
a=[list(input()) for _ in range(N)]
visited=[[0 for _ in range(M+1)] for _ in range(N+1)]
res1,res2=0,0
def go(sx,sy):
    q=deque()
    q.append((sx,sy))
    visited[sx][sy]=1
    y_cnt,w_cnt=0,0
    global res1,res2
    while q:
        x,y=q.popleft()
        if a[x][y]=='o':
            y_cnt+=1
        elif a[x][y]=='v':
            w_cnt+=1
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M) and not visited[n_x][n_y] and a[n_x][n_y]!='#':
                visited[n_x][n_y]=1
                q.append((n_x,n_y))
    if y_cnt>w_cnt:
        res1+=y_cnt
    else:
        res2+=w_cnt
for i in range(N):
    for j in range(M):
        if a[i][j]!='#' and not visited[i][j]:
            go(i,j)
print(res1,res2)