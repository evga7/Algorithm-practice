import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)+7
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
#dx=[0,1,0,-1,-1,-1,1,1]
#dy=[1,0,-1,0,-1,1,1,-1]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
N,M=map(int,input().split())
a=list(map(int,input().split()))
c=[0 for _ in range(N+1)]
a.sort()
v=[]
def go(idx,cnt):
    if cnt==M:
        print(*v)
        return
    back=-1
    for i in range(N):
        if back==a[i]:continue
        back=a[i]
        v.append(a[i])
        go(i,cnt+1)
        v.pop()
go(0,0)