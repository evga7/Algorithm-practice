import heapq
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
#dx = [0, 0, 1, -1]
#dy = [1, -1, 0, 0]
dx = [0, 1,1,1]
dy = [1, 0,1,-1]
a=[list(map(int,input().split())) for _ in range(19)]
c=[[[0 for _ in range(19)] for _ in range(19)] for _ in range(4)]
def chk(x,y,op):
    for i in range(4):
        cnt=1
        n_x=x
        n_y=y
        v=[]
        v.append((y,x))
        for j in range(19):
            if c[i][n_x][n_y]:break
            c[i][n_x][n_y]=1
            n_x+=dx[i]
            n_y+=dy[i]
            if not is_inside(n_x,n_y,19,19):break
            if a[n_x][n_y]==op:
                cnt+=1
                v.append((n_y, n_x))
            else:
                break
        if cnt==5:
            v.sort()
            print(op)
            print(v[0][1]+1,v[0][0]+1)
            exit(0)
for i in range(19):
    for j in range(19):
        if a[i][j]:
            chk(i,j,a[i][j])
print(0)