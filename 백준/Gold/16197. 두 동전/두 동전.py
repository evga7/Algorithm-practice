dx = [-1,1,0,0]  # 위 아 오 왼
dy = [0,0,1,-1]
# dx = [-1,-2,-2,-1,1,2,2,1]  # 오 왼 위 아
# dy = [-2,-1,1,2,2,1,-1,-2]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
visited=[[[[0 for _ in range(M+1)] for _ in range(N+1)] for _ in range(M+1)] for _ in range(N+1)]
q=[]
x1,y1,x2,y2=-1,0,-1,0
for i in range(N):
    for j in range(M):
        if a[i][j]=='o':
            if x1==-1:
                x1,y1=i,j
            else:
                x2,y2=i,j
def chk(x1,y1,x2,y2):
    if not is_inside(x1,y1,N,M) and is_inside(x2,y2,N,M):
        return True
    elif is_inside(x1,y1,N,M) and not is_inside(x2,y2,N,M):
        return True
    return False
q.append((0,x1,y1,x2,y2))
visited[x1][y1][x2][y2]=1
while q:
    cost,x,y,x2,y2=heapq.heappop(q)
    if cost>=10:continue
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        n_x2=x2+dx[i]
        n_y2=y2+dy[i]
        if is_inside(n_x,n_y,N,M) and a[n_x][n_y]=='#':
            n_x,n_y=x,y
        if is_inside(n_x2,n_y2,N,M) and a[n_x2][n_y2]=='#':
            n_x2,n_y2=x2,y2
        if chk(n_x,n_y,n_x2,n_y2):
            print(cost+1)
            exit(0)
        if is_inside(n_x,n_y,N,M) and is_inside(n_x2,n_y2,N,M) and not visited[n_x][n_y][n_x2][n_y2]:
            visited[n_x][n_y][n_x2][n_y2]=1
            heapq.heappush(q,(cost+1,n_x,n_y,n_x2,n_y2))
print(-1)