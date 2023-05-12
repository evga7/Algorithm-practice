dx=[0,0,1,-1]
dy=[1,-1,0,0]
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
res1=0
res2=0

while True:
    cnt=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cnt+=1
    
    if not cnt:
        break
    res1+=1
    res2=cnt
    q = deque()
    q.append((0, 0))
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    while q:
        x,y=q.popleft()
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M) and not visited[n_x][n_y]:
                visited[n_x][n_y]=1
                if arr[n_x][n_y]:
                    arr[n_x][n_y]=0
                else:
                    q.append((n_x,n_y))




print(res1,res2)