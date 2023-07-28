import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
a=list(map(int,input().split()))
v=[]
visited=[0 for _ in range(8)]
res=0
def go(cnt):
    if cnt==N:
        global res
        s=0
        for i in range(N-1):
            s+=abs(v[i]-v[i+1])
        res=max(res,s)
        return
    for i in range(N):
        if visited[i]:continue
        visited[i]=1
        v.append(a[i])
        go(cnt+1)
        visited[i]=0
        v.pop()
go(0)
print(res)