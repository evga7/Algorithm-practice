import sys
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
N=int(input())
a=[]
for i in range(1,N+1):
    a.append(i)
visited=[0 for _ in range(N+1)]
b=[]
def go(cnt):
    if cnt==N:
        print(*b)
        return
    for i in range(N):
        if visited[i]:continue
        visited[i]=1
        b.append(i+1)
        go(cnt+1)
        visited[i]=0
        b.pop()
go(0)