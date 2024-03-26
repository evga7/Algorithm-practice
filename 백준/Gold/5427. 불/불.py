dx = [1, -1, 0, 0]  # 아 위 오 왼
dy = [0, 0, 1, -1]
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M


import copy
import bisect
# sys.setrecursionlimit(100000)
import sys
import heapq
from collections import *
T=int(input())
flag=0
f = deque()
q = deque()
def sang_go():
    q2=deque()
    global q
    while q:
        x,y=q.popleft()
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if not is_inside(n_x,n_y,N,M):
                global flag
                flag=1
                break
            if a[n_x][n_y]=='.' and not visited[n_x][n_y]:
                visited[n_x][n_y]=1
                q2.append((n_x,n_y))
    q=copy.deepcopy(q2)
def fire_go():
    q2=deque()
    global f
    while f:
        x,y=f.popleft()
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,M) and a[n_x][n_y]=='.':
                a[n_x][n_y]='*'
                q2.append((n_x,n_y))
    f=copy.deepcopy(q2)
def go():
    cnt=0
    global flag
    while True:
        cnt+=1
        fire_go()
        sang_go()
        if flag:
            print(cnt)
            break
        if not q:
            print("IMPOSSIBLE")
            break
while T:
    T-=1
    flag=0
    sx,sy=0,0
    f.clear()
    q.clear()
    M,N=map(int,input().split())
    a=[list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if a[i][j]=='@':
                a[i][j]='.'
                q.append((i,j))
            elif a[i][j]=='*':
                f.append((i,j))
    visited=[[0 for _ in range(M+1)] for _ in range(N+1)]
    go()