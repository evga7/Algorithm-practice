import sys
def input():return sys.stdin.readline().rstrip() 
N,M=map(int,input().split())
v=[]
visited=[0 for _ in range(N+1)]
def go(cnt):
    if cnt==M:
        print(*v)
        return
    for i in range(N):
        if visited[i]:continue
        v.append(i+1)
        visited[i]=1
        go(cnt+1)
        visited[i]=0
        v.pop()
go(0)