import sys
#sys.setrecursionlimit(10000)
def input():return sys.stdin.readline().rstrip()
N=int(input())
g=[set() for _ in range(N+1)]
v=[]
visited=[0 for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    g[a].add(b)
    g[b].add(a)
a=list(map(int,input().split()))
if a[0]!=1:
    print(0)
    exit(0)
idx=1
def go(cur):
    global idx
    while idx<N and a[idx] in g[cur]:
        nxt=a[idx]
        idx+=1
        go(nxt)
go(1)
if idx==N:
    print(1)
else:
    print(0)