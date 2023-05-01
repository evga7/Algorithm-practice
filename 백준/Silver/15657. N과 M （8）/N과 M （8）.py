import sys
def input():return sys.stdin.readline().rstrip()
def is_inside(x,y,N,M):
    return 0<=x<N and 0<=y<M
N,M=map(int,input().split())
a=list(map(int,input().split()))
v=[0 for _ in range(M)]
a.sort()
def go(idx,cnt):
    if cnt==M:
        print(*v)
        return
    for i in range(idx,N):
        v[cnt]=a[i]
        go(i,cnt+1)
        v[cnt]=0
go(0,0)