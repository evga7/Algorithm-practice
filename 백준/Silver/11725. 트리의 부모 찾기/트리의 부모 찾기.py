import sys
sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
N=int(input())
p=[0 for _ in range(N+1)]
g=[[] for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
def go(cur,parent):
    if parent!=-1:
        p[cur]=parent
    for nxt in g[cur]:
        if not p[nxt]:
            go(nxt,cur)
go(1,-1)
for i in range(2,N+1):
    print(p[i])