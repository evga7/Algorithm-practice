dx = [-2,-2,0,0,2,2]  # 오 왼 위 아
dy = [-1,1,-2,2,-1,1]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
import copy
from collections import *
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
N=int(input())
sx,sy,ddx,ddy=map(int,input().split())
st=set()
q=[]
q.append((0,sx,sy))
while q:
    cost,x,y=heapq.heappop(q)
    if x==ddx and y==ddy:
        print(cost)
        exit(0)
    for i in range(6):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if is_inside(n_x,n_y,N,N) and not (n_x,n_y) in st:
            st.add((n_x,n_y))
            heapq.heappush(q,(cost+1,n_x,n_y))
print(-1)