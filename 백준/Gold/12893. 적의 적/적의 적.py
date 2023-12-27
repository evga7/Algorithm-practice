import sys
from collections import *
#sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
N,M=map(int,input().split())
g=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    g[a].append(b)
for i in range(1,N+1):
    q=deque()
    q.append(i)
    c=[0 for _ in range(N+1)]
    c[i]=1
    while q:
        cur=q.popleft()
        for nxt in g[cur]:
            if c[nxt]==0:
                c[nxt]=c[cur]*-1
                q.append(nxt)
            elif c[nxt]==c[cur]:
                print(0)
                exit(0)
print(1)
            
    