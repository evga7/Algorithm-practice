import sys
def input():return sys.stdin.readline().rstrip()
N,M=map(int,input().split())
g=[[] for _ in range(N+1)]
visited=[0 for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
def go(cur,cnt):
    if cnt==5:
        print(1)
        exit(0)
    for nxt in g[cur]:
        if visited[nxt]:continue
        visited[nxt]=1
        go(nxt,cnt+1)
        visited[nxt]=0
for i in range(N):
    visited[i]=1
    go(i,1)
    visited[i]=0
print(0)