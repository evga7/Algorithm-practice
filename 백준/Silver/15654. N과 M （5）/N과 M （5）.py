import sys
def input():return sys.stdin.readline().rstrip() 
N,M=map(int,input().split())
v=[]
a=list(map(int,input().split()))
visited=[0 for _ in range(N+1)]
a.sort()
def go(idx,cnt):
    if cnt==M:
        print(*v)
        return
    for i in range(N):
        if visited[i]:continue
        v.append(a[i])
        visited[i]=1
        go(i,cnt+1)
        visited[i] = 0
        v.pop()
go(1,0)
    