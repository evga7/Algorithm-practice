dx=[0,0,1,-1]
dy=[1,-1,0,0]
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import sys
import heapq
def input():return sys.stdin.readline().rstrip()
N,M,R=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
v=[[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        v[i][j]=a[i][j]
o={'E':0,'W':1,'S':2,'N':3}
res=0
def go(x,y,op):
    q=deque()
    q.append((x,y,v[x][y]-1))
    v[x][y]=0
    global res
    while q:
        cur_x,cur_y,cost=q.popleft()
        res+=1
        for i in range(cost):
            cur_x+=dx[o[op]]
            cur_y+=dy[o[op]]
            if is_inside(cur_x,cur_y,N,M) and v[cur_x][cur_y]:
                q.append((cur_x,cur_y,v[cur_x][cur_y]-1))
                v[cur_x][cur_y]=0

for i in range(R):
    x,y,op=input().split()
    x=int(x)
    y=int(y)
    go(x-1,y-1,op)
    x,y=map(int,input().split())
    v[x-1][y-1]=a[x-1][y-1]
print(res)
for i in range(N):
    for j in range(M):
        if v[i][j]:
            print('S',end=' ')
        else:
            print('F',end=' ')
    print('')