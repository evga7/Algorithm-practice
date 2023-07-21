dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
from collections import *
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
import sys
def input(): return sys.stdin.readline().rstrip()
res1=0
res2=0
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
visited=[[0 for _ in range(M)] for _ in range(N)]
def go(sx,sy):
    global res1,res2
    q=deque()
    q.append((sx,sy))
    k_cnt=0
    v_cnt=0
    while q:
        x,y=q.popleft()
        if a[x][y]=='k':
            k_cnt+=1
        elif a[x][y]=='v':
            v_cnt+=1
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M) and not visited[n_x][n_y] and a[n_x][n_y]!='#':
                q.append((n_x,n_y))
                visited[n_x][n_y]=1
    if v_cnt>=k_cnt:
        res2+=v_cnt
    else:
        res1+=k_cnt

for i in range(N):
    for j in range(M):
        if a[i][j]!='#' and not visited[i][j]:
            visited[i][j]=1
            go(i,j)
print(res1,res2)