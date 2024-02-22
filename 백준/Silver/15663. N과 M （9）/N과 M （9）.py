import sys
def input():return sys.stdin.readline().rstrip() 
N,M=map(int,input().split())
v=[]
a=list(map(int,input().split()))
visited=[0 for _ in range(N+1)]
a.sort()
def go(cnt):
    if cnt==M:
        print(*v)
        return
    back=-1
    for i in range(N):
        if visited[i] or back==a[i]:continue
        visited[i]=1
        v.append(a[i])
        back=a[i]
        go(cnt+1)
        visited[i]=0
        v.pop()
go(0)