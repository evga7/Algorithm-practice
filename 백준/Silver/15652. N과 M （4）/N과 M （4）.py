import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
v=[0 for _ in range(M)]
a=[i+1 for i in range(N)]
def go(idx,cnt):
    if cnt==M:
        print(*v)
        return
    for i in range(idx,N):
        v[cnt]=a[i]
        go(i,cnt+1)
go(0,0)