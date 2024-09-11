dx = [0,0,-1,1]  # 오 왼 위 아
dy = [1,-1,0,0]
import heapq
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
from collections import *
import itertools
import sys
#sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
v=[]
for i in range(1,N-1):
    for j in range(1,N-1):
        v.append((a[i][j],i,j))
st=set()
res=987654321
def go(idx,cnt,s):
    if cnt==3:
        global res
        res=min(res,s)
        return
    if idx>=len(v):
        return
    cost,x,y=v[idx]
    f=1

    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if (n_x,n_y) in st:
            f=0
            break
    if f and not (x,y) in st:
        n_s=s+cost
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            st.add((n_x,n_y))
            n_s+=a[n_x][n_y]
        st.add((x,y))
        go(idx+1,cnt+1,n_s)
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            st.remove((n_x,n_y))
        st.remove((x,y))
    go(idx+1,cnt,s)
go(0,0,0)
print(res)