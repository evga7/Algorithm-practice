import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
v=[0 for _ in range(M)]
def go(cnt):
    if cnt==M:
        print(*v)
        return

    for i in range(N):
        v[cnt]=a[i]
        go(cnt+1)
        v[cnt]=0
go(0)