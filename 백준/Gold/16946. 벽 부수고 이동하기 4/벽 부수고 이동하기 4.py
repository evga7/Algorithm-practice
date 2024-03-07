dx = [-1,1,0,0]  # 위 아 오 왼
dy = [0,0,1,-1]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
import copy
from collections import *
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=[list(map(int,input())) for _ in range(N)]
visited=[[0 for _ in range(M+1)] for _ in range(N+1)]
cnt=0
m=defaultdict(int)
def go(sx,sy):
    global cnt
    cnt+=1
    q=deque()
    visited[sx][sy]=cnt
    q.append((sx,sy))
    c=0
    while q:
        x,y=q.popleft()
        c+=1
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M) and not a[n_x][n_y] and not visited[n_x][n_y]:
                visited[n_x][n_y]=cnt
                q.append((n_x,n_y))
    m[cnt]=c


for i in range(N):
    for j in range(M):
        if not a[i][j] and not visited[i][j]:
            go(i,j)
for i in range(N):
    for j in range(M):
        if a[i][j]:
            c=1
            st=set()
            for k in range(4):
                n_x=i+dx[k]
                n_y=j+dy[k]
                if is_inside(n_x,n_y,N,M) and not a[n_x][n_y] and not visited[n_x][n_y] in st:
                    st.add(visited[n_x][n_y])
                    c+=m[visited[n_x][n_y]]
            print(c%10,end='')
        else:
            print(0,end='')
    print('')