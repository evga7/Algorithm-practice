import math
from collections import *
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
dx=[0,1,0,-1,-1,-1,1,1]
dy=[1,0,-1,0,-1,1,1,-1]
N,M=map(int,input().split())
a=list(map(int,input().split()))
st=set()
def chk(num):
    if num==1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if not num%i:
            return False
    return True
def go(idx,cnt,s):
    if cnt==M:
        if chk(s):
            st.add(s)
        return
    if idx==N:
        return
    go(idx+1,cnt,s)
    go(idx+1,cnt+1,s+a[idx])
go(0,0,0)
res=sorted(list(st))
if not res:
    print(-1)
else:
    print(*res)