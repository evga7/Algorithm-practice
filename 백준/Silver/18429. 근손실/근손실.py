import sys
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
a=list(map(int,input().split()))
res=0
visited=[0 for _ in range(N+1)]
def go(w,cnt):
    if w<500:
        return
    if cnt==N:
        global res
        if w>=500:
            res+=1
        return
    for i in range(N):
        if visited[i]:continue
        visited[i]=1
        go(w+a[i]-M,cnt+1)
        visited[i]=0
go(500,0)
print(res)