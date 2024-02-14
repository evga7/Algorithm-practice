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
N,M,X,Y,K=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(N)]
b=list(map(int,input().split()))
c=[0 for _ in range(7)]
jx,jy=1,1
def dice_go(dir):
    if dir==0:
        c[1],c[3],c[6],c[4]=c[3],c[6],c[4],c[1]
    elif dir==1:
        c[3],c[6],c[4],c[1]=c[1],c[3],c[6],c[4]
    elif dir==2:
        c[1], c[5], c[6], c[2] = c[2], c[1], c[5], c[6]
    else:
        c[2], c[1], c[5], c[6] = c[1], c[5], c[6], c[2]
def go(dir):
    global X,Y
    n_x=X+dx[dir]
    n_y=Y+dy[dir]
    if not is_inside(n_x,n_y,N,M):
        return
    dice_go(dir)
    X,Y=n_x,n_y
    if not a[X][Y]:
        a[X][Y]=c[6]
    else:
        c[6]=a[X][Y]
        a[X][Y]=0
    print(c[1])
for cur in b:
    go(cur-1)