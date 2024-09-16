import heapq
import itertools
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
#dx=[0,1,0,-1,-1,-1,1,1]
#dy=[1,0,-1,0,-1,1,1,-1]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
N,M=map(int,input().split())
a=[list(input()) for _ in range(N)]
T=int(input())
st=[[] for _ in range(M+1)]
def go(sx,sy,s_pos):
    x=sx
    y=sy
    if a[x][y]=='X':return
    while is_inside(x,y,N,M):
        n_x=x+1
        n_y=y
        f=0
        st[s_pos].append((x, y))
        if is_inside(n_x,n_y,N,M):
            if a[n_x][n_y]=='X':
                break
            elif a[n_x][n_y]=='O':
                if is_inside(x,y-1,N,M) and is_inside(n_x,y-1,N,M) and a[x][y-1]=='.' and a[n_x][y-1]=='.':
                    f=1
                    x,y=n_x,y-1
                elif is_inside(x,y+1,N,M) and is_inside(n_x,y+1,N,M) and a[x][y+1]=='.' and a[n_x][y+1]=='.':
                    f=1
                    x,y=n_x,y+1
                else:
                    break
        else:
            break
        if not f:
            x,y=n_x,n_y
    a[x][y]='O'
for i in range(T):
    pos=int(input())
    if st[pos-1]:
        sx,sy=st[pos-1].pop()
    else:
        sx,sy=0,pos-1
    while st[pos-1] and a[sx][sy]=='O':
        sx, sy = st[pos - 1].pop()
    if a[sx][sy]!='O':
        go(sx,sy,pos-1)

for i in range(N):
    for j in range(M):
        print(a[i][j],end='')
    print('')


