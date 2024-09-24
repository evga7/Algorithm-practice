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
g=defaultdict(int)
N=int(input())
a=list(map(int,input().split()))
ss=sum(a)
a.sort()
st=set()
c=[0 for _ in range(N+1)]
def go(idx,s):
    if 1<=s<=ss:
        st.add(s)
    if idx==N:
        return
    go(idx+1,s+a[idx])
    go(idx + 1, s - a[idx])
    go(idx+1,s)
        
go(0,0)
print(ss-len(st))