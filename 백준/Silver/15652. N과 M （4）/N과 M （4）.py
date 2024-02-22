import sys
def input():return sys.stdin.readline().rstrip() 
N,M=map(int,input().split())
v=[]
visited=[0 for _ in range(N+1)]
def go(idx,cnt):
    if cnt==M:
        print(*v)
        return
    for i in range(idx,N+1):
        v.append(i)
        go(i,cnt+1)
        v.pop()
go(1,0)