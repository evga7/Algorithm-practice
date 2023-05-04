import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
a=list(map(int,input().split()))
v=[]
a.sort()
visi=[0 for _ in range(N)]
def go(cnt):
    if cnt==M:
        print(*v)
        return
    for i in range(N):
        if visi[i]:continue
        visi[i]=1
        v.append(a[i])
        go(cnt+1)
        visi[i]=0
        v.pop()
go(0)