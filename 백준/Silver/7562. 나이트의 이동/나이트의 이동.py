import itertools
import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
#dx=[0,1,0,-1]
#dy=[1,0,-1,0]
dx=[-1,-2,-2,-1,1,2,2,1]
dy=[-2,-1,1,2,2,1,-1,-2]
T=int(input())
while T:
    T-=1
    N=int(input())
    sx,sy=map(int,input().split())
    ex, ey = map(int, input().split())
    q=deque()
    st=set()
    q.append((0,sx,sy))
    st.add((sx,sy))
    while q:
        cost,x,y=q.popleft()
        if x==ex and y==ey:
            print(cost)
            break
        for i in range(8):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if is_inside(n_x,n_y,N,N) and not (n_x,n_y) in st:
                st.add((n_x,n_y))
                q.append((cost+1,n_x,n_y))

